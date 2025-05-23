from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FloatField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, NumberRange

class LoginForm(FlaskForm):
    username = StringField('اسم المستخدم', validators=[DataRequired()])
    password = PasswordField('كلمة المرور', validators=[DataRequired()])
    submit = SubmitField('تسجيل الدخول')

class ProductForm(FlaskForm):
    name = StringField('اسم المنتج', validators=[DataRequired()])
    description = TextAreaField('وصف المنتج')
    price = FloatField('السعر', validators=[DataRequired(), NumberRange(min=0)])
    image = FileField('صورة المنتج (اختياري للتعديل)', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'الرجاء تحميل صور فقط!')])
    submit = SubmitField('حفظ')

class CheckoutForm(FlaskForm):
    customer_name = StringField('الاسم الكامل', validators=[DataRequired()])
    customer_address = TextAreaField('عنوان التوصيل الكامل', validators=[DataRequired()])
    customer_phone = StringField('رقم الهاتف', validators=[DataRequired()])
    submit = SubmitField('تأكيد الطلب والدفع عند الاستلام')
