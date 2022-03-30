from flask import Flask, Response, jsonify, render_template
import mysql.connector

from Gmail_Resources.gmail import sendmail
from calendar_resources.Calendar import cal_requests
from reCAPTCHA_resources.reCAPTCHA import Widgets
from youtube.youtube_api import YoutubeAPI
from translate.translate_api import translate_text

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config["RECAPTCHA_PUBLIC_KEY"] = "6LdPNysfAAAAAAcz55krT3CLz-RO6kdUCy5ay-kx"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6LdPNysfAAAAAOTJN3IzODHa4VQVjfYdHrrB3c_l"


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
    return render_template('translate.html', result=translate_text('ro', value))


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
