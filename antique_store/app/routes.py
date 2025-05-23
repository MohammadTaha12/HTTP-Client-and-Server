from flask import Blueprint, render_template, session, redirect, url_for, flash
from .models import Product, Order, OrderItem # Import Order and OrderItem
from .forms import CheckoutForm # Import CheckoutForm
from app import db # Import db instance

# Create a Blueprint for general routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index')
def index():
    products = Product.query.filter_by(is_sold=False).order_by(Product.date_added.desc()).all()
    return render_template('index.html', title='متجر جوست', products=products)

@main_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', title=f"{product.name} - متجر جوست", product=product)

@main_bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart_items = session.get('cart', {})
    if not cart_items:
        flash('سلتك فارغة. الرجاء إضافة منتجات قبل إتمام الشراء.', 'info')
        return redirect(url_for('cart.view_cart'))

    form = CheckoutForm()
    total_price = sum(item['price'] * item['quantity'] for item in cart_items.values())

    if form.validate_on_submit():
        # Re-check product availability before creating order
        for product_id_str in list(cart_items.keys()): # Iterate over a copy of keys for safe removal
            product_id = int(product_id_str)
            product_check = Product.query.get(product_id)
            if not product_check or product_check.is_sold:
                flash(f"عفواً، المنتج '{cart_items[product_id_str]['name']}' لم يعد متاحاً وتم حذفه من سلتك.", "danger")
                cart_items.pop(product_id_str)
                session['cart'] = cart_items # Update session
                session.modified = True
        
        # If cart becomes empty after re-check, redirect
        if not cart_items:
            flash('لم يعد أي من المنتجات في سلتك متاحاً. الرجاء المحاولة مرة أخرى.', 'warning')
            return redirect(url_for('cart.view_cart'))
            
        # Recalculate total price after validation
        total_price = sum(item['price'] * item['quantity'] for item in cart_items.values())

        order = Order(customer_name=form.customer_name.data,
                      customer_address=form.customer_address.data,
                      customer_phone=form.customer_phone.data,
                      total_amount=total_price,
                      status='قيد المعالجة')
        db.session.add(order)
        db.session.flush() # Get order.id

        for product_id_str, item_data in cart_items.items():
            product_id = int(product_id_str)
            product = Product.query.get(product_id) # Already checked availability, this is for creating OrderItem
            
            # This check is slightly redundant due to the loop above, but good for safety
            if product and not product.is_sold: 
                order_item = OrderItem(order_id=order.id,
                                         product_id=product.id,
                                         quantity=item_data['quantity'], # Should be 1
                                         price_at_purchase=item_data['price'])
                db.session.add(order_item)
                product.is_sold = True # Mark product as sold
            # No else needed here as unavailable items were removed from cart_items

        db.session.commit()
        session.pop('cart', None)
        session.modified = True
        flash(f'تم استلام طلبك بنجاح! رقم طلبك هو #{order.id}. سنتواصل معك قريباً لتأكيد التوصيل.', 'success')
        return redirect(url_for('main.index')) # Or a dedicated thank you page

    return render_template('shop/checkout.html', form=form, cart_items=cart_items, total_price=total_price, title="إتمام الشراء")
