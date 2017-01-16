from app import *
from pprint import pprint


#region print user list
from model.user import User
users = User.query.all()

d = {
  'data': users
}
pprint(d)
#endregion print user list


##region print user_email list
from model.user_email import UserEmail
userEmails = UserEmail.query.all()

d = []
for ue in userEmails:
  item = ue.toDict()

  #region followFK
  item['owner'] = ue.owner.toDict()
  #endregion followFK

  d.append(item)

d = {
  'data': d
}

pprint(d)
##endregion print user_email list


##region add/delete user
user_name = 'user333'

#region add
from model.user import User
user = User()
user.user_name = user_name

from app import db_session
db_session.add(user)
db_session.commit()

d={
  'message': 'Added user %s' % user_name,
  'data': user.toDict(),
}
pprint(d)
#endregion add

#region delete the added user
from model.user import User
users = User.query.filter_by(user_name=user_name).all()

from app import db_session
for user in users:
  db_session.delete(user)
db_session.commit()

d={
  'message': 'Deleted user %s' % user.user_name,
  'data': user.toDict(),
}
pprint(d)
#endregion delete the added user

##endregion add/delete user


##region user with address
user_name = 'uuserWithAddreess'

from model.user import User
user = User.query.filter_by(user_name=user_name).first()
if not user: raise Exception('User not found user_name=%s' % user_name)

##region raw from db
d={
  'message': 'User with address',
  'data': user.toDict(),
}
pprint(d)
#endregion raw from db

#region followFK
item = user.toDict()
item['billingAddress']  = user.billingAddress.toDict()  if user.billingAddress else None
item['shippingAddress'] = user.shippingAddress.toDict() if user.shippingAddress else None

d = {
  'message': 'User with address - followFK',
  'data': item,
}
pprint(d)
#endregion followFK

pass
##endregion user with address
