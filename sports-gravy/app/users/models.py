import datetime
from app import db, bcrypt, uploaded_photos
from sqlalchemy.ext.hybrid import hybrid_property
from flask_security import UserMixin, RoleMixin 


class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)#nullable=False, 
    email = db.Column(db.String(255), nullable=False, unique=True)
    _password = db.Column(db.String(255), nullable=False, default='') #hybrid column
    confirmed = db.Column(db.Boolean(), default=False)
    confirmed_at = db.Column(db.DateTime)
    date_created = db.Column(db.DateTime,  default=datetime.datetime.utcnow)
    date_modified = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    last_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(45))
    current_login_at = db.Column(db.DateTime)
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer, default=0)
    profile = db.relationship('Profile', uselist=False)
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))
    

    @hybrid_property 
    def password(self):
        return self._password 

    @password.setter 
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def has_role(self, role):
        if role in self.roles:
            return True
        else:
            return False

    def get_id(self):
        return unicode(self.id)


    def __repr__(self):
        return "<username-{}".format(self.username)

# Define the Role DataModel
class Role(db.Model, RoleMixin):
    __tablename__ = "role"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Role %r>' % self.name

class UserRoles(db.Model):
    __tablename__ = "user_roles"
    
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer(), primary_key=True)
    avatar = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id, ondelete='CASCADE'))

    @property 
    def imgsrc(self):
        return uploaded_photos.url(self.avatar)
 







