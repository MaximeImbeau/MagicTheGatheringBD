import pymysql
import pymysql.cursors
from flask import Flask, render_template, request

app = Flask(__name__)
image_sources = []


@app.route("/catalog")
def get_cards():
    global image_sources

    image_sources = []

    conn = pymysql.connect(host='localhost', user='root', password='kroot', db='testdb')
    cmd = 'SELECT * FROM cards' + ';'
    cur = conn.cursor()
    cur.execute(cmd)

    data = cur.fetchall()

    for d in data:
        image_sources.append(d[4])

    return render_template('catalog.html', card_info=list(data), image_sources=image_sources)


@app.route("/search", methods=['GET', 'POST'])
def search():
    return render_template('search.html')


@app.route("/results", methods=['GET', 'POST'])
def results():
    global image_sources

    image_sources = []

    name = request.form.get('card-name')
    colors = request.form.getlist('color')
    rarity = '"' + request.form.get('rarity') + '"'
    card_type = '"' + request.form.get('type') + '"'

    name_query = '"' + '%{}%'.format(name) + '"'
    colors = tuple(colors)

    conn = pymysql.connect(host='localhost', user='root', password='kroot', db='testdb')
    cmd = 'SELECT * FROM cards NATURAL JOIN card_colors'

    if name_query != '"%%"':
        cmd = cmd + ' WHERE name LIKE {} '.format(name_query)

        if rarity != '""':
            cmd = cmd + 'AND rarity={} '.format(rarity)

            if card_type != '""':
                cmd = cmd + 'AND type={} '.format(card_type)
            else:
                if len(colors) > 1:
                    cmd = cmd + 'AND color IN {}'.format(colors) + ';'
                if len(colors) == 1:
                    cmd = cmd + 'AND color={}'.format('"' + colors[0] + '"') + ';'
        else:
            if card_type != '""':
                cmd = cmd + 'AND type={}'.format(card_type)
            else:
                if len(colors) > 1:
                    cmd = cmd + 'AND color IN {}'.format(colors) + ';'
                if len(colors) == 1:
                    cmd = cmd + 'AND color={}'.format('"' + colors[0] + '"') + ';'

    else:
        if rarity != '""':
            cmd = cmd + ' WHERE rarity={} '.format(rarity)

            if card_type != '""':
                cmd = cmd + 'AND type={} '.format(card_type)
            else:
                if len(colors) > 1:
                    cmd = cmd + 'AND color IN {}'.format(colors) + ';'
                if len(colors) == 1:
                    cmd = cmd + 'AND color={}'.format('"' + colors[0] + '"') + ';'
        else:
            if card_type != '""':
                cmd = cmd + ' WHERE type={}'.format(card_type)
            else:
                if len(colors) > 1:
                    cmd = cmd + ' WHERE color IN {}'.format(colors) + ';'
                if len(colors) == 1:
                    cmd = cmd + ' WHERE color={}'.format('"' + colors[0] + '"') + ';'

    cur = conn.cursor()
    cur.execute(cmd)

    data = cur.fetchall()

    if len(data) == 0:
        return render_template('results.html', no_results='No results available.')

    for d in data:

        if d[4] not in image_sources:
            image_sources.append(d[4])

    return render_template('results.html', card_info=list(data), image_sources=image_sources)


@app.route("/")
def home():
    return render_template('navbar.html')


if __name__ == "__main__":
    app.run()
