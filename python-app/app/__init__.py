#region app config
SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost/sandbox_sqlalchemy?charset=utf8'
#endregion app config

###region database

##region setup db connection
#region create db_session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(SQLALCHEMY_DATABASE_URI)

db_session = scoped_session(
  sessionmaker(bind=engine)
)
#endregion create db_session

import sqlalchemy as db

#region make `relationship()` callable via `db.relationship()`
from sqlalchemy.orm import relationship
'''ref. http://stackoverflow.com/a/5356035/248616'''
import sys
setattr(sys.modules['sqlalchemy'], 'relationship', relationship)
#endregion make `relationship()` callable via `db.relationship()`

pass
##endregion setup db connection

#region import model class
from model.user       import User
from model.user_email import UserEmail
from model.address    import Address
#endregion import model class

pass #TODO make this block into separate file e.g. database.py
###endregion database
