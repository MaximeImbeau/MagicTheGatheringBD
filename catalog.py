import pymysql
import pymysql.cursors
from flask import Flask, render_template

app = Flask(__name__)
card_names = []
image_sources = []


@app.route("/catalog")
def get_cards():
    global card_names
    global image_sources

    card_names = []
    image_sources = []

    conn = pymysql.connect(host='localhost', user='root', password='kroot', db='testdb')
    cmd = 'SELECT * FROM Cards' + ';'
    cur = conn.cursor()
    cur.execute(cmd)

    data = cur.fetchall()

    for d in data:
        card_names.append(d[0])
        image_sources.append(d[5])

    return render_template('catalog.html', names=card_names, image_sources=image_sources)


@app.route("/")
def home():
    return render_template('navbar.html')


if __name__ == "__main__":
    app.run()
