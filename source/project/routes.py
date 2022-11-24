import pandas as pd
from project import app,bcrypt, db
from flask import Flask ,render_template, flash ,redirect,url_for,request, Response
from flask_login import login_user, logout_user, login_required
from project.model import User, History
from project.form import Register_User,SignInForm
from project.chatbot import chatbot
from datetime import datetime, time
import project.ml_model as mod
import numpy as np


#HOME PAGE ROUTE
@app.route('/',methods=['POST','GET'])
def home():
	form = SignInForm();

	if form.validate_on_submit():
	#validating the sign-in form
		user = User.query.filter_by(email_id=form.email_id.data).first()
		return redirect(url_for('user'))

		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			#return redirect(url_for('User_Page',name_f=name))
			print("Signed in")
			return redirect(url_for('user'))

		else:
			#if login fails
			flash(f'Login Unsuccesful. Please check your email id or password','danger')

	return render_template('home.html',form = form)

#USER PAGE
@app.route('/user',methods=['GET','POST'])
def user():
	return render_template('user.html')

@app.route("/get")
def get_bot_response():
	model = mod.Mlmodel()
	sympts_data = np.reshape(np.zeros(132),(1,132))
	class_names = list(model.return_symp_names())
	dis = ''
	user = request.args.get('text')
	if(request.args.get('medi') == 'y'):
		if(user in class_names):
				sympts_data[0][class_names.index(user)] =1
				dis = model.test_model(sympts_data)
				return("You might have "+dis)

		elif(user == ''):
			return('Type something..')

		else:
			return("Sorry couldn't find")

	elif(request.args.get('medi') == 'n'):
		resp = str(chatbot.get_response(user))
		if(resp == 'Do you feel?'):return '' 
		return str(chatbot.get_response(user))

	else:
		return('I am sorry, but I do not understand. I am still learning.')



#REGISTER ROUTE
@app.route('/register',methods=['POST','GET'])
def register():
	form = Register_User()

	if form.is_submitted():
		print("submited")

	if(form.validate_on_submit()):

		user = User.query.filter_by(email_id=form.email_id.data).first()
		pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

		user1 = User(Name=form.Name.data,Age = int(form.Age.data),
			Gender = form.Gender.data,Mobile_number = int(form.Mobile_number.data),
			email_id = form.email_id.data,
			password = pwd)
		db.session.add(user1)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		flash(f'Error Occured','danger')

	return render_template('register.html',form =form)

#LOGOUT ROUTE
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('home'))

