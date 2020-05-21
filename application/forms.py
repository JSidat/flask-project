from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

ex = [('Back squat','Back squat'),('Deadlift','Deadlift'), ('Bench press', 'Bench press')]

class PostForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
        )
    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=2, max=30)
            ]
        )   
    exercise_name = SelectField('exercise_name', choices= ex)
            
        
    maximum_lift = IntegerField('Biggest Lift(kg)',
            validators = [
                DataRequired()
            ]
        )
    notes = StringField('workout notes',
            validators = [
                DataRequired()
            ]
        )

    submit = SubmitField('Post Workout')


