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

  ##region relationship obj
  owner = relationship(User)

  #more verbose syntax as below - used when multiple FK+PK exist on both sides of referrer+referee tables
  #owner = relationship(User, foreign_keys=[user_id])
  #owner = relationship(User, foreign_keys=[user_id], remote_side=[User.id])

  ##endregion relationship obj
