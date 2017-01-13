from app import app
from flask import jsonify

@app.route('/')
def index():
  return '122 flaask appp'


@app.route('/user/list')
def user_list():
  from model.user import User
  users = User.query.all()
  users = [u.toDict() for u in users]

  d = {
    'data': users
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616
