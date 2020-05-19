from application import db


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    exercise_name = db.Column(db.String(20), db.ForeignKey('exercises.exercise_name'), nullable=False)
    maximum_lift = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(500), nullable=False)
    exercises = db.relationship('Exercise', backref='workout', lazy='dynamic')

    def __repr__(self):
     return ''.join([
         'User: ', self.first_name, ' ', self.last_name, '\r\n',
         'Exercise: ', self.exercise_name, '\r\n', self.maximum_lift, 'kg',
         'Notes: ', self.notes

         ])

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return ''.join([
            'Exercise: ', self.exercise_id, self.exercise_name
        ])

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

    def __repr__(self):
        return ''.join([
            'Exercise: ', self.exercise_id, self.workout_id, '\r\n', self.exercise_name
        ])


