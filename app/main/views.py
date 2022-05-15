from curses import flash
from flask import render_template,abort,redirect, url_for
from . import main 
from flask_login import login_required,current_user
from ..models import User,Blog,Comment
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db



@main.route ('/',methods=['GET','POST'])
def index():
    
    blogs = Blog.query.all()
    message = "Hello World" 

    return render_template('index.html', message=message,blogs=blogs)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = current_user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)



# add new blog
@main.route('/newblog', methods=['GET', 'POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        blog = Blog(blog_title=blog_form.blog_title.data,
                    content=blog_form.content.data,
            )
        db.session.add(blog)
        db.session.commit()
      
        return redirect(url_for('.index'))
    return render_template('newblog.html', blog_form=blog_form,user = current_user)

#comment
@main.route('/blog/<int:blog_id>/comment', methods=['GET', 'POST'])
@login_required 
def comment(blog_id):

    comment_form = CommentForm()

    blog = Blog.query.get(blog_id)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comment(comment=comment,blog_id = blog_id)
        new_comment.save_comment()
       
       
        return redirect(url_for('main.comment',blog_id=blog_id))

    all_comments =  Comment.query.filter_by(blog_id=blog_id).all()
    title = f'{blog.blog_title}'
    return render_template('comment.html',comment_form=comment_form,blog=blog,comment=all_comments,title=title)
