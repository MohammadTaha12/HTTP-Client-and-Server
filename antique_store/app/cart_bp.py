from flask import Blueprint, session, redirect, url_for, flash, render_template, abort
from app.models import Product # Assuming Product model is in app/models.py

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    
    if product.is_sold:
        flash('عذراً، هذا المنتج تم بيعه بالفعل.', 'danger')
        return redirect(url_for('main.product_detail', product_id=product_id))
        
    cart = session.get('cart', {})
    product_id_str = str(product_id) # Use string for dict key

    if product_id_str in cart:
        flash('المنتج موجود بالفعل في سلتك.', 'info')
    else:
        cart[product_id_str] = {
            'name': product.name,
            'price': product.price,
            'image': product.image_filename,
            'quantity': 1 # Each antique item is unique, so quantity is 1
        }
        session['cart'] = cart
        session.modified = True # Important to mark session as modified
        flash('تمت إضافة المنتج إلى السلة بنجاح!', 'success')
        
    return redirect(url_for('cart.view_cart'))

@cart_bp.route('/cart')
def view_cart():
    cart_items = session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart_items.values())
    # The template path will be 'shop/cart.html'
    return render_template('shop/cart.html', cart_items=cart_items, total_price=total_price, title="سلة المشتريات")

@cart_bp.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    product_id_str = str(product_id) # Use string for dict key

    if product_id_str in cart:
        del cart[product_id_str]
        session['cart'] = cart
        session.modified = True
        flash('تم حذف المنتج من السلة.', 'success')
    else:
        flash('المنتج غير موجود في السلة.', 'warning')
        
    return redirect(url_for('cart.view_cart'))
