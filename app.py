from flask import Flask, Response, jsonify, render_template, request
import mysql.connector
from google.cloud.sql.connector import connector
import sqlalchemy

from Gmail_Resources.gmail import sendmail
from calendar_resources.Calendar import cal_requests
from reCAPTCHA_resources.reCAPTCHA import Widgets
from youtube.youtube_api import YoutubeAPI
from translate.translate_api import translate_text
from places.places_api import PlacesAPI

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config["RECAPTCHA_PUBLIC_KEY"] = "6LdPNysfAAAAAAcz55krT3CLz-RO6kdUCy5ay-kx"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6LdPNysfAAAAAOTJN3IzODHa4VQVjfYdHrrB3c_l"


@app.route('/')
def index():
    # configure Cloud SQL Python Connector properties
    def getconn():
        conn = connector.connect(
            "cc-tema3-345518:europe-north1:database",
            "pymysql",
            user="root",
            password="12345",
            db="tema3-db"
        )
        return conn

    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )

    # query or insert into Cloud SQL database
    with pool.connect() as db_conn:
        # query database
        result = db_conn.execute("SELECT * from translate").fetchall()

        # Do something with the results
        # for row in result:
        #     print(row)

    return render_template("index.html", data=result)


@app.route('/translate2/<value>')
def translate(value):
    mydb = mysql.connector.connect(
        host="34.88.254.196",
        user="root",
        password="12345",
        database="tema3-db",
    )
    result = translate_text('ro', value)
    original = value
    translated = result['translatedText']
    fromLanguage = result['detectedSourceLanguage']
    toLanguage = 'ro'


    mycursor = mydb.cursor()

    mycursor.execute(f"INSERT INTO translate (original, translated, from_lang, to_lang) VALUES (\"{original}\", \"{translated}\", \"{fromLanguage}\", \"{toLanguage}\")")

    mydb.commit()
    mydb.close()
    return render_template('translate.html', result=result, db='Translation added to database')

@app.route('/translate/<value>')
def translate2(value):

    return render_template('translate.html', result=translate_text('ro', value))



@app.route('/gmail', methods=("GET", "POST"))
def sendgmail():
    form = Widgets()
    if request.method == "GET":
        return render_template('gmail.html', form=form)
    if request.method == "POST":
        if (request.form["g-recaptcha-response"] != ''):
            name = request.form["name"]
            sendmail("Hello " + name + "\n")
            return render_template("gmail_sent.html")
        else:
            return render_template("invalid.html")


@app.route('/calendar')
def calendar():

    str = cal_requests()
    return render_template('calendar.html', value=list(str))


@app.route('/youtube/<value>')
def youtube_api(value):
    yapi = YoutubeAPI(value)

    return render_template('youtube.html', video_id=yapi.get_first_from_search())


@app.route('/places/<value>')
def places(value):
    places_api = PlacesAPI()
    result = places_api.get_place(value)
    return render_template('places.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
