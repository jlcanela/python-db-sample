import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Application(Base):
    __tablename__ = 'application'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class Log(Base):
    __tablename__ = 'log'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    message = Column(String(250))
    application_id = Column(Integer, ForeignKey('application.id'))
    application = relationship(Application)
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('mysql+mysqlconnector://root:MYSQL_ROOT_PASSWORD@localhost/logging')
# user="root",passwd="MYSQL_ROOT_PASSWORD", auth_plugin="mysql_native_password")

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# Insert a Person in the person table
new_app = Application(name='sample-app')
session.add(new_app)
session.commit()
 
current_app = session.query(Application).first()
print("application name:", current_app.name)

# Insert an Address in the address table
new_log= Log(message='a log', application=new_app)
session.add(new_log)
session.commit()

logs = session.query(Log).all()
for log in logs:
	print(log.application.name, ":", log.message)
