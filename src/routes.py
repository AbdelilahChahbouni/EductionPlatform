
from flask import render_template , url_for, flash , redirect , request
from src.forms import LoginForm , RegisterForm , UpdateProfileForm
from src.models import User , Lesson , Course
from src import app , bcr , db
from flask_login import login_user , logout_user , current_user  , login_required
import secrets , os
from PIL import Image
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


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _ , f_ext = os.path.splitext(form_picture.filename)
    picture_name = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/images" , picture_name)
    output_size =(150 , 150) 
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_name





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

@app.route("/dashboard" , methods=["GET" , "POST"])
@login_required
def dashboard():
    form_profile = UpdateProfileForm()
    if form_profile.validate_on_submit():
        if form_profile.picture.data:
            picture_file = save_picture(form_profile.picture.data)
            current_user.image_profile = picture_file
        current_user.username = form_profile.username.data
        current_user.email = form_profile.email.data
        current_user.bio = form_profile.bio.data
        db.session.commit()
        flash("You Profile is Updated Successfuly" , "success")
        return redirect(url_for("dashboard"))
    elif request.method == "GET":
        form_profile.username.data = current_user.username
        form_profile.email.data = current_user.email
        form_profile.bio.data = current_user.bio

    image_file = url_for("static", filename=f"images/{current_user.image_profile}") 
    return render_template("dashboard.html" , title="Dashboard" , profile_form=form_profile , image_file=image_file)

