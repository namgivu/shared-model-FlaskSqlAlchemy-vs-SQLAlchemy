from base_model import BaseModel
from app import db

from model.user_email import UserEmail


class User(BaseModel):
  #table mapping
  __tablename__ = "users"

  #column mapping
  id = db.Column(db.Integer, primary_key=True)
  user_name = db.Column(db.Text)

  ##region relationship obj
  #emails = db.relationship(UserEmail, foreign_key=[User.id], remote_side=[UserEmail.id], use_list=True) #TODO How to create the `backref` directly on referred model class instead of from the referrer class?
  ##endregion relationship obj
