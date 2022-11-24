#forms
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TimeField, DateField,DecimalField,SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Length,EqualTo, ValidationError,Email
from project.model import User


########################## REGISTER USER #############################
class Register_User(FlaskForm):

	Name        = StringField("Name",validators=[DataRequired()
		,Length(min=2,max=20)])


	Age = DecimalField("Age",validators=[DataRequired()])

	Gender =  SelectField("Exam Name",validators=[DataRequired()],choices=[('Male','Male'),('Female','Female'),
		('Others','Others')
		])
	
	Mobile_number       = DecimalField("Mobile_number",validators=[DataRequired()])


	email_id    		= EmailField("email_id",validators=[DataRequired(),Email()])

	password    		= PasswordField('Password',validators=[DataRequired()])

	submit      		= SubmitField('submit')

	def validate_mail(self, email_id):

		user = User.query.filter_by(email_id=email_id.data).all()
		if user:
			raise ValidationError('The User is already present!!')
			flash(f'Already Present','danger')

########################## SIGN IN FORM #############################			
class SignInForm(FlaskForm):

	email_id    		= EmailField("email_id",validators=[DataRequired(),Email()])

	password    		= PasswordField('Password',validators=[DataRequired()])

	submit      		= SubmitField('submit')

