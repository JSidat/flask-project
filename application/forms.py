from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
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
    notes = StringField('Workout Notes',
            validators = [
                DataRequired(),
                Length(min=2)
            ]
        )
    exercise = StringField('Exercise',
            validators = [
                DataRequired()
            ]
        )
    weight_lifted = StringField('Biggest Lift(kg)',
            validators = [
                DataRequired()
            ]
        )
    submit = SubmitField('Post Workout')


