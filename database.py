import csv
from app import db
#ip;domains;hostnames;version;org;port;data;country;city
class Hosts(db.Model):
    __tablename__ = 'hosts'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String)
    domains = db.Column(db.String)
    hostnames = db.Column(db.String)
    version = db.Column(db.String)
    org = db.Column(db.String)
    port = db.Column(db.String)
    data = db.Column(db.String)
    country = db.Column(db.String)
    city = db.Column(db.String)
    def __repr__(self):
        return '<User %r>' % self.id