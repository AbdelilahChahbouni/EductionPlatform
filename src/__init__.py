from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"]="0d97a641b022202ee46a9f48cdf6e15a3ee1dac999601d21cbe3143206c3664b"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
db = SQLAlchemy(app)
bcr = Bcrypt(app)
login_manger = LoginManager(app)
login_manger.login_view = 'login'
login_manger.login_message_category = 'info'
migrate = Migrate(app , db)
from src import routes