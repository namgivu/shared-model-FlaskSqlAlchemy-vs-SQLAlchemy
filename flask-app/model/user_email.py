from base_model import BaseModel
from app import db


class UserEmail(BaseModel):
  #table mapping
  __tablename__ = "user_emails"

  #column mapping
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  ##region relationship obj
  owner = db.relationship('User', back_populates='emails')

