from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms.fields import TextField
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired,Email


class ContactForm(Form):
    name = TextField(' Name', validators=[DataRequired()])
    subject = TextField('Subject', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    

