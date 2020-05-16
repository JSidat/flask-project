from application import db
from datetime import datetime

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    exercise = db.Column(db.String(20), nullable=False)
    maximum_lift = db.column(db.Integer(5), nullable=False)
    notes = db.Column(db.String(500), nullable=False)

    def __repr__(self):
     return ''.join([
         'User: ', self.first_name, ' ', self.last_name, '\r\n',
         'Exercise: ', self.exercise, '\r\n', self.maximum_lift, 'kg',
         'Notes: ', self.notes

        ])

