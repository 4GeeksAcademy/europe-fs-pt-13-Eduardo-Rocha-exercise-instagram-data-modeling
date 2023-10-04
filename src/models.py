import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    userpassword = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    user_bio = Column(String(250))
    ##privateAccount = Column(bool)

class Login(Base):
    __tablename__='login'
    id = Column(Integer, primary_key=True)
    userName = Column(String, ForeignKey('user.username'))
    password = Column(String, ForeignKey('user.userpassword'))
    login = relationship(User)

class Photo(Base):
    __tablename__='photo'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    location = Column(String(250))
    postId = Column(String, ForeignKey('post.id'))
    userId = Column(Integer, ForeignKey('user.id'))
    ##likes = Column(bool)
    photo = relationship(User)

class Comments(Base):
    __tablename__='comments'
    id = Column(Integer, primary_key=True)
    avatarUrl = Column(String(250))
    comment = Column(String(250))
    userId = Column(Integer, ForeignKey('user.id'))
    userName = Column(Integer, ForeignKey('user.username'))
    ##comments = relationship(Notifications)
    comments = relationship(Photo)

class Like(Base):
    __tablename__='like'
    id = Column(Integer, primary_key=True)
    avatarUrl = Column(String(250), nullable=False)
    userName = Column(Integer, ForeignKey('user.username'))
    ##like = relationship(Notifications)
    like = relationship(Photo)

class Notifications(Base):
    __tablename__='notifications'
    id = Column(Integer, primary_key=True)
    temps = Column(String(250), nullable=False)
    userId = Column(Integer, ForeignKey('user.id'))
    comments = relationship(User)
    comments = relationship(Comments)
    comments = relationship(Like)
    ##comments = relationship(Followers)

class Followers(Base):
    __tablename__='followers'
    id = Column(Integer, primary_key=True)
    followerId = Column(String(250), nullable=False)
    userId = Column(Integer, ForeignKey('user.id'))
    followers = relationship(Notifications)
    followers = relationship(User)

class Subscribes(Base):
    __tablename__='subscribes'
    id = Column(Integer, primary_key=True)
    subscriberId = Column(String(250), nullable=False)
    userId = Column(Integer, ForeignKey('user.id'))
    subscribes = relationship(User)

class Profile(Base):
    __tablename__='profile'
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    userId = Column(Integer, ForeignKey('user.id'))
    ##profile = relationship(Post)
    profile = relationship(Photo)
    profile = relationship(User)

class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    profileID = Column(String(250), nullable=False)
    userId = Column(Integer, ForeignKey('user.id'))
    post = relationship(User)
    post = relationship(Profile)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
