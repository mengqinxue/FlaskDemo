from datetime import datetime

from database import db

# CREATE TABLE user (ID int primarykey auto_increment,
#                    username varchar(20) not null,
#
class UserModule(db.Model):
    # db.Column(type, constraints)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    rts = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, password, phone):
        self.username = username
        self.password = password
        self.phone = phone

    def __str__(self):
        return self.username + ' ' + self.phone


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    gender = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.id + ' ' + self.name
