from base_model import BaseModel
import sqlalchemy as db
from sqlalchemy.orm import relationship

#region make `relationship()` callable via `db.relationship()`
'''ref. http://stackoverflow.com/a/5356035/248616'''
import sys
setattr(sys.modules['sqlalchemy'], 'relationship', relationship)
#endregion make `relationship()` callable via `db.relationship()`

from model.user import User

class UserEmail(BaseModel):
  #table mapping
  __tablename__ = "user_emails"

  #column mapping
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey(User.id))

  ##region relationship obj
  #owner = relationship(User) #original way via pure `sqlalchemy` module
  owner = db.relationship(User) #customized way

  #more verbose syntax as below - used when multiple FK+PK exist on both sides of referrer+referee tables
  #owner = db.relationship(User, foreign_keys=[user_id])
  #owner = db.relationship(User, foreign_keys=[user_id], remote_side=[User.id])

  ##endregion relationship obj
