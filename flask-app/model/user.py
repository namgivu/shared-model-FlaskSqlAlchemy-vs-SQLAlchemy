from base_model import BaseModel
from app import db


class User(BaseModel):
  #table mapping
  __tablename__ = "users"

  ##region column mapping
  id = db.Column(db.Integer, primary_key=True)
  user_name = db.Column(db.Text)
  primary_email_id = db.Column(db.Integer, db.ForeignKey('user_emails.id') ) #TODO How to use model class instead of physical table name
  ##endregion column mapping

  ##region relationship obj
  emails = db.relationship('UserEmail',
                           primaryjoin='User.id==UserEmail.user_id',
                           back_populates='owner')

  primaryEmail = db.relationship('UserEmail',
                                 primaryjoin='User.primary_email_id==UserEmail.id')
  ##endregion relationship obj
