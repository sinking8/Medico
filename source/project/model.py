#models
from datetime import datetime
from project import db, login_manager
from flask_login import UserMixin
from sqlalchemy_utils import EmailType


@login_manager.user_loader
def get_user(user_id):
	return User.query.get(user_id)

class User(db.Model, UserMixin):
	id                    = db.Column(db.Integer,primary_key=True)
	Name                  = db.Column(db.String(40),nullable=False)
	Age    		          = db.Column(db.Integer,nullable=False)
	Gender                = db.Column(db.String(2),nullable=False)
	Mobile_number 		  = db.Column(db.Integer,nullable=False)
	email_id      		  = db.Column(EmailType,nullable=False)
	password      		  = db.Column(db.String(40),nullable=False)

class History(db.Model, UserMixin):

	id                    = db.Column(db.Integer,primary_key =True)
	Name                  = db.Column(db.String(40))
	History               = db.Column(db.String(40))
