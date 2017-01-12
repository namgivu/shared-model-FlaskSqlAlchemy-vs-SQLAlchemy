Get started
---
Shared model object in Flask-SqlAlchemy http://flask-sqlalchemy.pocoo.org/2.1/ vs pure SQLAlchemy http://www.sqlalchemy.org/

Notes
---
- Use mysql TEXT against VARCHAR
  <br>
  ref. http://stackoverflow.com/a/6404708/248616
  > Unless you need to index these columns (in which case VARCHAR is much faster) there is no reason to use VARCHAR over TEXT
  
Flask app
---
- install app's prerequisites
  ```
  $APP_HOME/flask-app/util/prerequisite.sh
  ```

- run app
  ```
  $APP_HOME/flask-app/util/run.sh
  ```

Python app
---
- run app
  ```
  $APP_HOME/python-app/util/run.sh
  ```

(the end)