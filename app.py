from flask import Flask, Response, jsonify, render_template
from flask_wtf import FlaskForm, RecaptchaField
import mysql.connector
from wtforms import StringField, RadioField, SelectField, TextAreaField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

from Gmail_Resources.gmail import sendmail
from calendar_resources.Calendar import cal_requests
from youtube.youtube_api import YoutubeAPI

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config["RECAPTCHA_PUBLIC_KEY"] = "6LdPNysfAAAAAAcz55krT3CLz-RO6kdUCy5ay-kx"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6LdPNysfAAAAAOTJN3IzODHa4VQVjfYdHrrB3c_l"

class Widgets(FlaskForm):
    recaptcha = RecaptchaField()
    name = StringField(label="Name", validators=[DataRequired()])

    radio = RadioField(label="Please select Your Programming language ",
                       choices=[('Python', "Python"), ["C++", "C++"]])

    select = SelectField(label='select', choices=[("1", "WebApp"), ("2", "Web Scrapping")])
    comments = TextAreaField(label="comments")
    date = DateTimeField(label="Birthday", format='%Y-%m-%d')

    submit = SubmitField(label="Submit")
# @app.route('/')
# def index():
#     # # print(mydb)
#     # mydb = mysql.connector.connect(
#     #     host="34.88.254.196",
#     #     user="root",
#     #     password="12345",
#     #     database="tema3-db",
#     # )
#     #
#     # mycursor = mydb.cursor()
#     #
#     # mycursor.execute("SELECT * FROM translate")
#     #
#     # myresult = mycursor.fetchall()
#
#     return render_template('index.html', mydb='myresult')

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/translate/<value>')
def translate(value):
    return render_template('translate.html', value=int(value))


@app.route('/gmail/<value>')
def gmail(value):
    print(value)
    form = Widgets()
    sendmail()
    return render_template('gmail.html', form=form)


@app.route('/calendar')
def calendar():

    str = cal_requests()
    return render_template('calendar.html', value=list(str))


@app.route('/youtube/<value>')
def youtube_api(value):
    yapi = YoutubeAPI(value)

    return render_template('youtube.html', video_id=yapi.get_first_from_search())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
