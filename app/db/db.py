from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, String, create_engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    uuid = Column(String(100), primary_key=True)
    name = Column(String(100))

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
