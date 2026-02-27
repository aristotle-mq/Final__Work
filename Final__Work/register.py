from flask_wtf import FlaskForm                                                 # Объект класса FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField         # Устанавлиается вместе с flask_wtf
from wtforms.validators import DataRequired, Email, Length, EqualTo


class MyRegisterForm(FlaskForm):
    login = StringField('Your login', validators=[DataRequired()])
    email = EmailField('Your email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8)])
    confirm = PasswordField('Password confirm', validators=[DataRequired(), EqualTo('password')])
    submit_reg = SubmitField('Start your free trial')

class MyAuthorizationForm(FlaskForm):
    login = StringField('Your login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8)])
    submit_auth = SubmitField('Authorization')