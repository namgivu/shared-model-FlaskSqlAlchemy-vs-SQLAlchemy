#region print user list
from model.user import User
users = User.query.all()

d = {
  'data': users
}
print d
#endregion print user list
