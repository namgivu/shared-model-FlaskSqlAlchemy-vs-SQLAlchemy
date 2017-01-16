from base_model import BaseModel
from app import db


class Address(BaseModel):
  #table mapping
  __tablename__ = "addresses"

  ##region column mapping
  id = db.Column(db.Integer, primary_key=True)
  street_address = db.Column(db.Text)
  ##endregion column mapping
