from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



apps = Flask(__name__)

#database
apps.config["SECRET_KEY"] = "jygfiyhdbkhfb4h5bk3425#^9##^%"
apps.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdatabase.db'
apps.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(apps)
bcrypt = Bcrypt(apps)
login_manager = LoginManager(apps)
login_manager.login_view = "login"
login_manager.login_message = "you have not logged in, please login to access"
login_manager.login_message_category = "info"


from project import routers

