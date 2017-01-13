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

#region add owner field
d = []
for ue in userEmails:
  item = ue.toDict()
  item['owner'] = ue.owner.toDict()
  d.append(item)
#endregion add owner field

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

from app import db
db.add(user)
db.commit()

d={
  'message': 'Added user %s' % user_name,
  'data': user.toDict(),
}
pprint(d)
#endregion add

#region delete the added user
from model.user import User
users = User.query.filter_by(user_name=user_name).all()

from app import db
for user in users:
  db.delete(user)
db.commit()

d={
  'message': 'Deleted user %s' % user.user_name,
  'data': user.toDict(),
}
pprint(d)
#endregion delete the added user

##endregion add/delete user