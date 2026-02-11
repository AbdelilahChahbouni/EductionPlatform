from src import db
from datetime import datetime



class User(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    fname = db.Column(db.String(25) , nullable=False)
    lname = db.Column(db.String(25) , nullable=False)
    username = db.Column(db.String(25) , nullable=False , unique=True)
    email = db.Column(db.String(125) , nullable=False , unique=True)
    password = db.Column(db.String(60) , nullable=False)
    image_profile = db.Column(db.String(20) , default="default.png")
    lesson = db.relationship("Lesson" , backref='author' , lazy=True)

    def __repr__(self):
        return f"user {self.fname} , {self.lname} , {self.username} , {self.email}"
    

class Lesson(db.Model):
    id = db.Column(db.Integer , primary_key= True)
    title = db.Column(db.String(25) , nullable=False)
    date_posted = db.Column(db.DateTime , nullable=False , default=datetime.utcnow)
    content = db.Column(db.Text , nullable=False)
    thumbnail = db.Column(db.String(25) , nullable=False , default="default_thumbnail.jpg")
    slug= db.Column(db.String(25) , nullable=False)
    user_id = db.Column(db.Integer , db.ForeignKey("user.id") , nullable=False)
    course_id = db.Column(db.Integer , db.ForeignKey("course.id"), nullable=True)

    def __repr__(self):
        return f"Lesson {self.title} , {self.date_posted}"
    
class Course(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(20) , unique=True , nullable=False)
    description = db.Column(db.String(130) , nullable=False)
    icon = db.Column(db.String(30) , nullable=False , default="default_icon.jpg")
    lesson = db.relationship("Lesson" , backref="course_name" , lazy=True)

    def __repr__(self):
        return f"Course {self.title}"


