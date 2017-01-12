from base_model import BaseModel
import sqlalchemy as db


class User(BaseModel):
  __tablename__ = "users"

  id   = db.Column(db.Integer, primary_key=True)
  user_name = db.Column(db.Text)

