from app import app
from app import db
from flask import jsonify
from flask import request

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


@app.route('/user/add', methods=['POST'])
def user_add():
  #region data from param
  user_name = request.values.get('user_name')
  #endregion data from param

  #do adding new user
  from model.user import User
  user = User()
  user.user_name = user_name

  #store to db
  db.session.add(user)
  db.session.commit()

  #output
  d = {
    'message': 'Added new user user_name=%s' % user_name,
    'data': user.toDict(),
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616


@app.route('/user/delete', methods=['POST'])
def user_delete():
  #region data from param
  user_id = request.values.get('user_id')
  #endregion data from param

  #get user obj from user_id
  from model.user import User
  user = User.query.get(user_id)
  if not user: raise Exception('User not found user_id=%s' % user_id)

  #do delete & store to db
  db.session.delete(user)
  db.session.commit()

  #output
  d = {
    'message': 'Deleted user user_id=%s' % user_id,
    'data': user.toDict(),
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616


@app.route('/user/update', methods=['POST'])
def user_update():
  #region data from param
  user_id   = request.values.get('user_id')
  user_name = request.values.get('user_name')
  #endregion data from param

  #get user obj from user_id
  from model.user import User
  user = User.query.get(user_id)
  if not user: raise Exception('User not found user_id=%s' % user_id)

  #do update
  user.user_name = user_name

  #store to db
  db.session.add(user)
  db.session.commit()

  #output
  d = {
    'message': 'Updated user user_id=%s' % user_id,
    'data': user.toDict(),
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
