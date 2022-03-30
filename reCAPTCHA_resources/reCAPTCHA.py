from wtforms import StringField, RadioField, SelectField, TextAreaField, DateTimeField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm, RecaptchaField




class Widgets(FlaskForm):
    recaptcha = RecaptchaField()
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired()])

    radio = RadioField(label="Please select Your Programming language ",
                       choices=[('Python', "Python"), ["C++", "C++"]])

    select = SelectField(label='select', choices=[("1", "WebApp"), ("2", "Web Scrapping")])
    comments = TextAreaField(label="comments")
    date = DateTimeField(label="Birthday", format='%Y-%m-%d')

    submit = SubmitField(label="Submit")