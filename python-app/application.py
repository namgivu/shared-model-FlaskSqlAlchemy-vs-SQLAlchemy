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
