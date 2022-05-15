from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy import text

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    profile_pic_path = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))

    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    
    @property
    def password(self):
        # block access to password
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}'



class Blog(db.Model):
    __tablename__ = 'blogs'

    id= db.Column(db.Integer,primary_key=True)
    blog_title = db.Column(db.String(255))
   
    content = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    author = db.Column(db.Integer,db.ForeignKey("users.id"))

    comments = db.relationship('Comment',backref = 'blog',lazy = "dynamic")
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_blog(cls,id):
        blogs = Blog.query.filter_by(id=id).all()
        return blogs

    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.order_by(text('-id')).all()
        return blogs



    def __repr__(self):
        return f'Blog {self.blog_title}'

class Comment(db.Model):
    ___tablename__='comments'

    id = db.Column(db.Integer,primary_key = True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment = db.Column(db.String(255))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).all()
        return comments
    @classmethod
    def get_all_comments(cls,id):
        comments = Comment.query.order_by(text('-id')).all()
        return comments

    