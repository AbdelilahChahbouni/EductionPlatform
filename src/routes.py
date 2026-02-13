
from flask import render_template , url_for, flash , redirect , request
from src.forms import LoginForm , RegisterForm
from src.models import User , Lesson , Course
from src import app , bcr , db
from flask_login import login_user , logout_user , current_user  , login_required

lessons = [{
    'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
]

courses = [
{
        'name': 'Python',
        'icon': 'python.svg',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Data Analysis',
        'icon': 'analysis.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Machine Learning',
        'icon': 'machine-learning.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Web Design',
        'icon': 'web.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Blockchain',
        'icon': 'blockchain.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Tips & Tricks',
        'icon': 'idea.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

]



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html" , lessons=lessons , courses=courses)

@app.route("/about")
def about():
    return render_template("about.html" , title="About")

@app.route("/register" , methods=['GET' , 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcr.generate_password_hash(form.password.data)
        user = User(fname=form.fname.data , lname=form.lname.data , username=form.username.data , email=form.email.data , password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('you have created account successfully' , 'success')
        return redirect(url_for("login"))

    return render_template("register.html" , form=form , title="Register")

@app.route("/login" , methods=["GET" , "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcr.check_password_hash(user.password , form.password.data):
            login_user(user , remember=form.remember.data)
            next_page = request.args.get('next')
            flash("you have been logged in succesfully" , "success")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("you have been logged in unsuccessfuly , check the password or the email" , "danger")

    return render_template("login.html" , form=form , title="Register")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html" , title="Dashboard")

