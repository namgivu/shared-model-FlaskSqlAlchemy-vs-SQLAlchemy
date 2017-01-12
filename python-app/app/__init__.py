#region app config
SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost/sandbox_sqlalchemy?charset=utf8'
#endregion app config

#region setup db connection
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(SQLALCHEMY_DATABASE_URI)

db = scoped_session(
  sessionmaker(bind=engine)
)
#endregion setup db connection
