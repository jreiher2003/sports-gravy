import os 
from flask import Flask
from flask_mail import Mail
from flask_script import Manager 
from flask_caching import Cache 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_uploads import UploadSet, configure_uploads, IMAGES, UploadNotAllowed, patch_request_class
# from flask_admin import Admin, BaseView, AdminIndexView 
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__) 
app.config.from_object(os.environ['APP_SETTINGS']) 
uploaded_photos = UploadSet('photos', IMAGES)
configure_uploads(app, uploaded_photos)
mail = Mail(app)  # Initialize Flask-Mail
db = SQLAlchemy(app) # Initialize Flask-SQLAlchemy
bcrypt = Bcrypt(app)
cache = Cache(app)
manager = Manager(app) 

from temp_filters import dateify, datetimefilter, urlify, datetimefilter_f, game_time, game_date, game_day, roundify
app.jinja_env.filters["dateify"] = dateify
app.jinja_env.filters["datetimefilter"] = datetimefilter
app.jinja_env.filters["urlify"] = urlify
app.jinja_env.filters["datetimefilter_f"] = datetimefilter_f
app.jinja_env.filters["game_time"] = game_time
app.jinja_env.filters["game_date"] = game_date
app.jinja_env.filters["game_day"] = game_day
app.jinja_env.filters["roundify"] = roundify


# from app.admin.models import AdminPage, UserAdmin 
# admin = Admin(app, name="Peer 2 Peer", template_mode="bootstrap3", index_view=AdminPage())
# admin.add_view(UserAdmin(Users, db.session, endpoint="users_"))
# admin.add_view(ModelView(Profile, db.session))
# admin.add_view(ModelView(Role, db.session))
# admin.add_view(ModelView(UserRoles, db.session))


# from app.users.views import users_blueprint
# app.register_blueprint(users_blueprint) 
from app.home.views import home_blueprint
app.register_blueprint(home_blueprint) 
from app.nfl.views import nfl_blueprint
app.register_blueprint(nfl_blueprint) 





