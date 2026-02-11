
from flask import render_template , url_for, flash , redirect 
from src.forms import LoginForm , RegisterForm
from src.models import User , Lesson , Course
from src import app

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
    form = RegisterForm()
    if form.validate_on_submit():
        flash('you have created account successfully' , 'success')
        return redirect(url_for("login"))

    return render_template("register.html" , form=form , title="Register")

@app.route("/login" , methods=["GET" , "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "reda@gmail.com" and form.password.data == "Reda%%900":
            flash("you have been logged in succesfully" , "success")
            return redirect(url_for("home"))
        else:
            flash("you have been logged in unsuccessfuly , check the password or the email" , "danger")

    return render_template("login.html" , form=form , title="Register")