from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegistrationForm(FlaskForm):
    email = EmailField('Email Address', validators=[DataRequired()])
    name = StringField('Username', validators=[DataRequired(), Length(min=2)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("SIGN ME UP")

class LoginForm(FlaskForm):
    email = EmailField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("LET ME IN")

class CommentForm(FlaskForm):
    body = CKEditorField('Comments', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit')