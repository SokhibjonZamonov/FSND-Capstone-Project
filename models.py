import os
from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "capstone"
#database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres2001','localhost:5432', database_name)
database_path = "postgres://uvkikegfqtrvpm:5f24008f3936ae8d6c6599b7a57912a41c73df35589ff42d819f806ec498ea91@ec2-50-17-90-177.compute-1.amazonaws.com:5432/dal8d2o27vccbq"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Movie(db.Model):
	__tablename__ = 'movies'
	id = Column(Integer, primary_key = True)
	title = Column(String(30))
	release_date = Column(Date)
	director = Column(String(30))

	def __init__(self, title, release_date, director):
		self.title = title
		self.release_date = release_date
		self.director = director


	def insert(self):
	    db.session.add(self)
	    db.session.commit()
  
	def update(self):
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def format(self):
		return {
		'id': self.id,
		'title': self.title,
		'release_date': self.release_date,
		'director': self.director
		}

class Actor(db.Model):
	__tablename__ = 'actors'
	id = Column(Integer, primary_key = True)
	first_name = Column(String(10))
	last_name = Column(String(10))
	age = Column(Integer)
	gender = Column(String(6))

	def __init__(self, first_name, last_name, age, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
	
	def insert(self):
	    db.session.add(self)
	    db.session.commit()
  
	def update(self):
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()


	def format(self):
		return {
		'id': self.id,
		'first_name': self.first_name,
		'last_name': self.last_name,
		'age': self.age,
		'gender': self.gender
		}