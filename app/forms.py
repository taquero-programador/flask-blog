from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	"formulario de inicio de sesion"
	# declaradas como variables de clases
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_user = BooleanField('Remember me')
	submit = SubmitField('Sign In')
