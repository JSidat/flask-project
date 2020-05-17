from application import app, db
from flask import render_template, redirect, url_for
from application.forms import PostForm
from application.models import Workout


@app.route('/')
@app.route('/home')
def home():
    postData =  Workout.query.all()
    return render_template('home.html', title='Home', posts=postData)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/workout')
def workout():
    form = PostForm()
    if form.validate_on_submit():
        postData =  Workout(
                first_name = workout.first_name.data,
                last_name = workout.last_name.data,
                exercise_name = workout.exercise_name.data,
                maximum_lift = workout.maximum_lift.data,
                notes = workout.notes.data
            )

        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        print(form.errors)
        return render_template('workout.html', title='Workout', form=form)
            
