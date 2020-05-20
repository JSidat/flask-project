from application import app, db
from flask import render_template, redirect, url_for, flash
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
        return render_template('add_workout.html', title='Add Workout',
                                form=form, legend = 'New Post')

@app.route('/workouts')
def workouts():
    postData =  Workout.query.all()
    return render_template('workouts.html', title='Workouts', workout=postData)


@app.route('/post/<post_id>')
def post(post_id):
    post = Workout.query.get_or_404(post_id)
    return render_template('post.html', title='Workout', post=post)


@app.route('/post/<post_id>/update', methods=['GET', 'POST'])
def update_post(post_id):
    post = Workout.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.first_name = form.first_name.data
        post.last_name = form.last_name.data
        post.exercise_name = form.exercise_name.data
        post.maximum_lift = form.maximum_lift.data
        post.notes = form.notes.data
        db.session.commit()
        flash('Your workout has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))     
    form.first_name.data = post.first_name
    form.last_name.data = post.last_name
    form.exercise_name.data = post.exercise_name
    form.maximum_lift.data = post.maximum_lift
    form.notes.data = post.notes 
    return render_template('add_workout.html', title='Update Post',
                            form=form, legend = 'Update Post')

