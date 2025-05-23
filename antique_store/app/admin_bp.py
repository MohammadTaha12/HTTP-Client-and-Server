from flask import Blueprint, render_template, redirect, url_for, flash, current_app, abort, request
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
from sqlalchemy.orm import joinedload # For eager loading
from app import db
from app.models import Product, Order, OrderItem, ORDER_STATUSES # Import ORDER_STATUSES
from app.forms import ProductForm

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html', title='لوحة تحكم المدير')

# Product Management Routes (from previous tasks)
@admin_bp.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    form = ProductForm()
    form.submit.label.text = 'إضافة منتج'
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        price = form.price.data
        image_filename = None
        if form.image.data:
            f = form.image.data
            image_filename = secure_filename(f.filename)
            upload_path = current_app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_path):
                os.makedirs(upload_path, exist_ok=True)
            f.save(os.path.join(upload_path, image_filename))
        product = Product(name=name, description=description, price=price, image_filename=image_filename)
        db.session.add(product)
        db.session.commit()
        flash('تمت إضافة المنتج بنجاح!', 'success')
        return redirect(url_for('admin.list_products'))
    return render_template('admin/add_product.html', form=form, title='إضافة منتج جديد')

@admin_bp.route('/products')
@login_required
def list_products():
    products = Product.query.all()
    return render_template('admin/list_products.html', products=products, title='قائمة المنتجات')

@admin_bp.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    form.submit.label.text = 'حفظ التعديلات'
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        if form.image.data:
            upload_path = current_app.config['UPLOAD_FOLDER']
            if product.image_filename:
                old_image_path = os.path.join(upload_path, product.image_filename)
                if os.path.exists(old_image_path):
                    try:
                        os.remove(old_image_path)
                    except OSError as e:
                        flash(f'خطأ في حذف الصورة القديمة: {e}', 'danger')
            f = form.image.data
            new_image_filename = secure_filename(f.filename)
            if not os.path.exists(upload_path):
                os.makedirs(upload_path, exist_ok=True)
            f.save(os.path.join(upload_path, new_image_filename))
            product.image_filename = new_image_filename
        db.session.commit()
        flash('تم تحديث المنتج بنجاح!', 'success')
        return redirect(url_for('admin.list_products'))
    return render_template('admin/edit_product.html', form=form, product=product, title='تعديل المنتج')

@admin_bp.route('/delete_product/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    if product.image_filename:
        upload_path = current_app.config['UPLOAD_FOLDER']
        image_path = os.path.join(upload_path, product.image_filename)
        if os.path.exists(image_path):
            try:
                os.remove(image_path)
            except OSError as e:
                flash(f'خطأ في حذف صورة المنتج: {e}', 'danger')
    db.session.delete(product)
    db.session.commit()
    flash('تم حذف المنتج بنجاح!', 'success')
    return redirect(url_for('admin.list_products'))

# Order Management Routes
@admin_bp.route('/orders')
@login_required
def list_orders():
    orders = Order.query.order_by(Order.order_date.desc()).all()
    return render_template('admin/list_orders.html', orders=orders, ORDER_STATUSES=ORDER_STATUSES, title='إدارة الطلبات')

@admin_bp.route('/order/<int:order_id>')
@login_required
def order_detail(order_id):
    order = Order.query.options(
        joinedload(Order.order_items).joinedload(OrderItem.product)
    ).get_or_404(order_id)
    return render_template('admin/order_detail.html', order=order, ORDER_STATUSES=ORDER_STATUSES, title=f'تفاصيل الطلب #{order.id}')

@admin_bp.route('/order/update_status/<int:order_id>', methods=['POST'])
@login_required
def update_order_status(order_id):
    order = Order.query.get_or_404(order_id)
    new_status_key = request.form.get('status')

    if new_status_key in ORDER_STATUSES:
        order.status = new_status_key
        # If status is 'Cancelled', mark products as not sold
        if new_status_key == 'Cancelled':
            for item in order.order_items:
                if item.product: # Check if product still exists
                    item.product.is_sold = False
            flash('تم إلغاء الطلب وإعادة المنتجات للمخزون.', 'info')
        db.session.commit()
        flash('تم تحديث حالة الطلب بنجاح!', 'success')
    else:
        flash('حالة الطلب غير صالحة.', 'danger')
    
    return redirect(url_for('admin.order_detail', order_id=order.id))
