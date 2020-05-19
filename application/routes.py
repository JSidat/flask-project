from application import app, db
from flask import render_template, redirect, url_for
from application.forms import PostForm
from application.models import Workout


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/add_workout', methods=['GET', 'POST'])
def add_workout():
    form = PostForm()
    if form.validate_on_submit():
        postData =  Workout(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                exercise_name = form.exercise_name.data,
                maximum_lift = form.maximum_lift.data,
                notes = form.notes.data
            )

        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('workouts'))

    else:
        print(form.errors)
        return render_template('add_workout.html', title='Add Workout', form=form)

@app.route('/workouts')
def workouts():
    postData =  Workout.query.all()
    return render_template('workouts.html', title='Workouts', workout=postData)


