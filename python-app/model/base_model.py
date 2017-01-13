from app import db_session
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
Base.query = db_session.query_property()


class BaseModel(Base):
  __abstract__ = True

  def __repr__(self):
    d = self.toDict()
    return str(d)

  def toDict(self):
    '''Convert model object to Python dict type - mapped-columns only'''
    d = {}
    columns = self._sa_class_manager.mapper.mapped_table.columns
    for col in columns:
      d[col.name] = getattr(self, col.name)
    return d
