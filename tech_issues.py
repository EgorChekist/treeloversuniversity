from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    curse = db.Column(db.String(1))
    level = db.Column(db.String(25))
    faculty = db.Column(db.String(50))