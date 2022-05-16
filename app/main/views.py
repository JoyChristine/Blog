from curses import flash
from flask import render_template,abort,redirect, url_for,request
from . import main 
from flask_login import login_required,current_user
from ..models import User,Blog,Comment
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db
from ..requests import get_randomquotes
# from ..email import mail_message


@main.route ('/',methods=['GET','POST'])
def index():
    
    blogs = Blog.query.all()
    message = "Hello World" 
    quotes = get_randomquotes()

    return render_template('index.html', message=message,blogs=blogs,quotes=quotes)



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
        content=blog_form.content.data
        blog_title=blog_form.blog_title.data
        new_blog = Blog(blog_title=blog_title,content=content,user=current_user)
        new_blog.save_blog()
        # blog = Blog(blog_title=blog_form.blog_title.data,content=blog_form.content.data,user_id=current_user.id)
        # db.session.add(blog)
        # db.session.commit()
      
        return redirect(url_for('main.index'))
        title = 'New Blog'
    return render_template('newblog.html', blog_form=blog_form,user = current_user)
# update blog
@main.route('/blog/<int:blog_id>/update', methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    blog_form = BlogForm()


    if blog.user != current_user:
        return render_template('four.html',message = 'Unauthorized Access')

    if blog_form.validate_on_submit():
        blog.blog_title = blog_form.blog_title.data
        blog.content = blog_form.content.data
        db.session.commit()
       
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        blog_form.blog_title.data = blog.blog_title
        blog_form.content.data = blog.content

    return render_template('newblog.html', blog_form=blog_form,blog=blog)

# delete blog
@main.route('/blog/delete/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()

    if blog.user != current_user:
         return render_template('four.html',message = 'Unauthorized Access')

    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('main.index'))





#comment
@main.route('/comment/<int:blog_id>', methods=['GET', 'POST'])
@login_required 
def comment(blog_id):

    comment_form = CommentForm()

    blog = Blog.query.get(blog_id)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comment(comment=comment,blog_id = blog_id,user=current_user)
        new_comment.save_comment()
       
       
        return redirect(url_for('main.comment',blog_id=blog_id))

    all_comments =  Comment.query.filter_by(blog_id=blog_id).all()
    # title = f'{blog.blog_title}'
    return render_template('comment.html',comment_form=comment_form,blog=blog,comment=all_comments)

# delete comment
@main.route('/comment/delete/<int:comment_id>', methods=['GET', 'POST'])
@login_required
def delete_comment(comment_id):
    
    comments = Comment.query.filter_by(id = comment_id).first()
    if comments.user != current_user:
            return render_template('four.html',message = 'Unauthorized Access')

    for comment in comments:
        db.session.delete(comment)
        db.session.commit()
    
    return redirect(url_for('main.comment',blog_id=comment.blog_id))