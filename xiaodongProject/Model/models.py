from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import HOSTNAME, PORT, DATABASE, USERNAME, PASSWORD


DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(50))

    def __repr__(self):
        return "<User(name: %s)>" % self.name


if __name__ == "__main__":
    Base.metadata.drop_all()
    Base.metadata.create_all()