from wtforms import TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write something about yourself',validators = [InputRequired()])
    submit = SubmitField('Submit')
class BlogForm(FlaskForm):
    blog_title = TextAreaField('Title',validators = [InputRequired()])
    content = TextAreaField('Content',validators = [InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment',validators = [InputRequired()])
    submit = SubmitField('Submit')