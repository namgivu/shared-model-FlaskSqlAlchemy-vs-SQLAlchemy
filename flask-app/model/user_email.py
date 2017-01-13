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

  ##region relationship obj
  owner = db.relationship(User)

  #more verbose syntax as below - used when multiple FK+PK exist on both sides of referrer+referee tables
  #owner = db.relationship(User, foreign_keys=[user_id])
  #owner = db.relationship(User, foreign_keys=[user_id], remote_side=[User.id])

  ##endregion relationship obj
