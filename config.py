import os

#get the projects root directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    #application configuration settings
    #sqlite database location
    SQLALCHEMY_DATABASE_URI = (f"sqlite:///{os.path.join(BASE_DIR,'database','tracker.db')}")

#    to disable unnessery object tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False