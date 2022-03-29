from flask import Flask, Response, jsonify, render_template
import mysql.connector
from Gmail_Resources.gmail import sendmail

app = Flask(__name__)


# @app.route('/')
# def index():
#     # print(mydb)
#     mydb = mysql.connector.connect(
#         host="34.88.254.196",
#         user="root",
#         password="12345",
#         database="tema3-db",
#     )
#
#     mycursor = mydb.cursor()
#
#     mycursor.execute("SELECT * FROM translate")
#
#     myresult = mycursor.fetchall()
#
#     return render_template('index.html', mydb=myresult)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/translate/<value>')
def translate(value):
    return render_template('translate.html', value=int(value))

@app.route('/gmail/<value>')
def gmail(value):
    sendmail()
    return render_template('gmail.html', value=int(value))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
