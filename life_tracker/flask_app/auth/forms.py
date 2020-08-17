from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    EqualTo,
    Optional,
    ValidationError,
)
from flask import (
    current_app as app,
)
from ...backend.models import (
    AppUser,
)


class RegistrationForm(FlaskForm):
    """User registration form."""
    first_name = StringField(
        'First name',
        validators=[
            DataRequired(),
        ],
    )
    last_name = StringField(
        'Last name',
        validators=[
            Optional(),
        ],
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            DataRequired(),
            Email(),
        ],
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Please choose a stronger password'),
        ],
    )
    confirm_password = PasswordField(
        'Confirm your password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.'),
        ],
    )
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = app.session.query(AppUser).filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('That email is already registered.')


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired()],
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
    )
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
