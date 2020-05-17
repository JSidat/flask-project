from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length



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
    exercise_name = StringField('Exercise Name',
            validators = [
                DataRequired()
            ]
        )
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


