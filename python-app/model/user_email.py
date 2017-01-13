from base_model import BaseModel
import sqlalchemy as db
from model.user import User
from sqlalchemy.orm import relationship


class UserEmail(BaseModel):
  #table mapping
  __tablename__ = "user_emails"

  #column mapping
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey(User.id))

  #relationship
  owner = relationship(User, foreign_keys=[user_id]) #TODO consider to add remote_side='App.developer_id'
