from base_model import BaseModel
from app import db


class User(BaseModel):
  #table mapping
  __tablename__ = "users"

  ##region column mapping
  id = db.Column(db.Integer, primary_key=True)
  user_name = db.Column(db.Text)
  ##endregion column mapping

  ##region relationship obj
  emails = db.relationship('UserEmail', back_populates='owner')
  ##endregion relationship obj

  ##region primary email
  #TODO How to add the 2nd FK to UserEmail? Currently this line break the emails+owner setup
  #primary_email_id = db.Column(db.Integer, db.ForeignKey('user_emails.id') )
  #primaryEmail = db.relationship('UserEmail', foreign_keys=[primary_email_id], primaryjoin='User.primary_email_id=UserEmail.id')
  ##endregion primary email
