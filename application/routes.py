from flask import render_template
from application import app


@app.route('/')
@app.route('/home')
def home():
    blogData = Posts.query.all()
    return render_template('home.html', title='Home', posts=blogData)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/post')
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData =  Posts(
                first_name = post.first_name.data,
                last_name = post.last_name.data,
                exercise = post.exercise.data,
                maximum_lift = post.maximum_lift.data
                notes = post.notes.data
            )

        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        print(form.errors)
        return render_template('post.html', title='Post', form=form)
            
