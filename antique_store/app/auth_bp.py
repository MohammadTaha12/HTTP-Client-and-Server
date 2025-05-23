from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db # Assuming db is initialized in app/__init__.py
from app.models import User # Assuming User model is in app/models.py
from app.forms import LoginForm # Assuming LoginForm is in app/forms.py

auth_bp = Blueprint('auth', __name__, url_prefix='/admin')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard')) # Assuming 'admin.dashboard' will exist
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully.', 'success')
            # Redirect to the admin dashboard, assuming it's 'admin.dashboard'
            # The actual admin dashboard route might be different or defined later
            next_page = url_for('admin.dashboard') 
            return redirect(next_page or url_for('admin.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('admin/login.html', form=form, title='Admin Login')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
