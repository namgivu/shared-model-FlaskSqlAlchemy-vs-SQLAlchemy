from base_model import BaseModel
from app import db
from model.user import User


class UserEmail(BaseModel):
  #table mapping
  __tablename__ = "user_emails"

  #column mapping
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey(User.id))

  #relationship
  owner = db.relationship(User, foreign_keys=[user_id]) #TODO consider to add remote_side='App.developer_id'
