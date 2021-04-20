from app import db
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import validates 
from werkzeug.security import generate_password_hash,check_password_hash

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