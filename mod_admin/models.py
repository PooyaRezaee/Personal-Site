from app import db
from sqlalchemy import Column,String,Integer,Text,DateTime
from sqlalchemy.orm import validates 
from werkzeug.security import generate_password_hash,check_password_hash
import datetime as dt

class Admin(db.Model):
    __tablename__ = 'Admin'

    Id = db.Column(Integer(),primary_key=True)
    UserName = Column(String(128),nullable=False,unique=True)
    Password = Column(String(128),nullable=False)

    @validates('Password')
    def validates_password(self,Token,value):
        return generate_password_hash(value)
    
    def check_password(self, password):
        return check_password_hash(self.Password,password)


class Settings(db.Model):
    __tablename__ = "settings"

    Id = db.Column(Integer(),primary_key=True)
    FullName = Column(String(64))
    AboutME = Column(Text)
    url_background = Column(String(256))
    url_profile = Column(String(256))

class Skills(db.Model):
    __tablename__ = "skills"

    Id = db.Column(Integer(),primary_key=True)
    Name = Column(String(32),unique=True)
    Value_skill = Column(Integer())

class Work_Sample(db.Model):
    __tablename__ = "work samples"

    Id = db.Column(Integer(),primary_key=True)
    title = Column(String(64),unique=True)
    url_image = Column(String(256))
    link = Column(Text)
class Documents(db.Model):
    __tablename__ = "documents"

    Id = db.Column(Integer(),primary_key=True)
    title = Column(String(64),unique=True)
    url_image = Column(String(256))
    link = Column(Text)

class Contact_way(db.Model):
    __tablename__ = "contact_way"

    Id = db.Column(Integer(),primary_key=True)
    text = Column(String(),unique=True)
    url_image = Column(String())
    link = Column(Text)

class Request(db.Model):
    __tablename__ = "Requests"

    Id = Column(Integer(),primary_key=True)
    ip = Column(String(64))
    method = Column(String(64))
    date = Column(DateTime(), default=dt.datetime.utcnow)