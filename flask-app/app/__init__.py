##region app creation
#app obj
from flask import Flask
app = Flask(__name__)

##region app config
#db connection
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/sandbox_sqlalchemy?charset=utf8'

#other settings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #to get rid of warning `UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future`

##endregion app config

##endregion app creation


#region setup db connection
from flask_sqlalchemy import SQLAlchemy #in place for DEPRECATED `from flask.ext.sqlalchemy import SQLAlchemy`

db = SQLAlchemy()
db.init_app(app)
#endregion setup db connection


#region load db model class
#region load db model class


#routing handler
import controller
