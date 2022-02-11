from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection"""


class EditUserProfileForm(FlaskForm):
    """Form to edit the details of a user"""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    image_url = StringField('Image URL')
    header_image_url = StringField('Header Image URL')
    bio = StringField('Bio')
    password = PasswordField('Password', validators=[Length(min=6)])

class LikesForm(FlaskForm):
    """Form for handling likes"""
    
    message_id = HiddenField("likes")