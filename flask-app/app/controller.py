from app import app
from flask import jsonify

@app.route('/')
def index():
  return '122 flaask appp'


##region User
@app.route('/user/list')
def user_list():
  from model.user import User
  users = User.query.all()
  users = [u.toDict() for u in users]

  d = {
    'data': users
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616
##endregion User


##region UserEmail
@app.route('/user_email/list')
def user_email_list():
  from model.user_email import UserEmail
  userEmails = UserEmail.query.all()

  #region add owner field
  d=[]
  for ue in userEmails:
    item = ue.toDict()
    item['owner'] = ue.owner.toDict()
    d.append(item)
  #endregion add owner field

  d = {
    'data': d
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616
##endregion UserEmail
