from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#create a sqlalchemy database object

db=SQLAlchemy()

class Issue(db.Model):
  #  stores info about issues reported by company
  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(100),nullable=False)
  description = db.Column(db.Text,nullable=False)
  priority = db.Column(db.String(20),nullable=False)
  status = db.Column(db.String(20),default="open")
  assigned_to = db.Column(db.String(100))
  created_data = db.Column(db.DateTime,default=datetime.utcnow)


class Vulnerability(db.Model):
  #stores info about security vulnerabilities
  id = db.Column(db.Integer,primary_key=True)   
  cve_number = db.Column(db.String(20),unique=True)
  severity = db.Column(db.String(20), nullable=False)
  affected_system = db.Column(db.String(100),nullable=False)
  description = db.Column(db.Text,nullable=False)
  status = db.Column(db.String(20),default="Open")
