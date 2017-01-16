from base_model import BaseModel
from app import db


class User(BaseModel):
  #table mapping
  __tablename__ = "users"

  #column mapping
  id = db.Column(db.Integer, primary_key=True)
  user_name = db.Column(db.Text)

  ##region relationship obj
  emails = db.relationship('UserEmail', back_populates='owner')
  ##endregion relationship obj
