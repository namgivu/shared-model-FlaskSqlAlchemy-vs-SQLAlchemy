from app import app
from app import db
from flask import jsonify
from flask import request
from util import get_param


@app.route('/')
def index():
  return '122 flaask appp'


##region User
@app.route('/user/list', methods=['GET'])
def user_list():
  from model.user import User
  users = User.query.all()
  users = [u.toDict() for u in users]

  d = {
    'data': users
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616


@app.route('/user/list/follow-fk', methods=['GET'])
def user_list_follow_fk():
  from model.user import User
  users = User.query.all()

  d=[]
  for u in users:
    item = u.toDict()
    item['primaryEmail'] = u.primaryEmail.toDict() if u.primaryEmail else None
    d.append(item)

  d = {
    'data': d
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
@app.route('/user_email/list', methods=['GET'])
def user_email_list_all():
  from model.user_email import UserEmail
  userEmails = UserEmail.query.all()

  d = {
    'data': [ue.toDict() for ue in userEmails]
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616


@app.route('/user_email/list/follow-fk', methods=['GET'])
def user_email_list_all_followFK():
  from model.user_email import UserEmail
  userEmails = UserEmail.query.all()

  #region add owner field
  d=[]
  for ue in userEmails:
    item = ue.toDict()
    item['owner'] = ue.owner.toDict() if ue.owner else None
    d.append(item)
  #endregion add owner field

  d = {
    'data': d
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616


@app.route('/user/email/list', methods=['GET'])
def user_email_list():
  #region data from param
  user_id   = request.values.get('user_id')
  #endregion data from param

  #get user obj from user_id
  from model.user import User
  user = User.query.get(user_id)
  if not user: raise Exception('User not found user_id=%s' % user_id)

  #do list email of a user
  from model.user_email import UserEmail
  userEmails = UserEmail.query.filter_by(user_id=user_id).all()

  d = {
    'data': [ue.toDict() for ue in userEmails]
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616


@app.route('/user_email/add', methods=['POST'])
def user_email_add():
  #region data from param
  user_name = request.values.get('user_name')
  email     = request.values.get('email')
  #endregion data from param

  #get user obj from user_name
  from model.user import User
  user = User.query.filter_by(user_name=user_name).first()
  if not user: raise Exception('User not found user_name=%s' % user_name)

  #check email already exist
  from model.user_email import UserEmail
  exist = UserEmail.query.filter_by(email=email).first()
  if exist: raise Exception('Email already taken email=%s' % email)


  #do adding new email
  userEmail = UserEmail()
  userEmail.owner = user
  userEmail.email = email

  #store to db
  db.session.add(userEmail)
  db.session.commit()

  #output
  d = {
    'message': 'Added new email {email} for user {user}'.format(email=email, user=user_name),
    'data': userEmail.toDict(),
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616


@app.route('/user_email/delete', methods=['POST'])
def user_email_delete():
  #region data from param
  #user_email_id = request.values.get('user_email_id')
  user_email_id = get_param(request, name='user_email_id', required=True)
  #endregion data from param

  #get userEmail obj from user_email_id
  from model.user_email import UserEmail
  userEmail = UserEmail.query.get(user_email_id)
  if not userEmail: raise Exception('UserEmail not found user_email_id=%s' % user_email_id)

  #do delete & store to db
  db.session.delete(userEmail)
  db.session.commit()

  #output
  d = {
    'message': 'Deleted user user_id=%s' % user_email_id,
    'data': userEmail.toDict(),
  }
  return jsonify(d) #return JSON in Flask ref. http://stackoverflow.com/a/13089975/248616
##endregion UserEmail
