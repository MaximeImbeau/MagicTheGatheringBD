from flask import Flask, render_template, request
import pymysql, pymysql.cursors
import uuid
import hashlib

app = Flask(__name__)
ProfileUtilisateur = {}

#For catalog
card_names = []
image_sources = []

selectedCards = []


@app.route("/")
def main():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def login():
    courriel = '"' + request.form.get('courriel') + '"'
    passe = request.form.get('motpasse')
    hashTable = hashlib.new('ripemd160')
    hashTable.update(passe.encode('utf-8'))


    conn= pymysql.connect(host='localhost',user='root', password='root',db='testdb')
    cmd='SELECT motpasse FROM Utilisateur WHERE courriel='+courriel+';'
    cur=conn.cursor()

    cur.execute(cmd)
    passeVrai = cur.fetchone()

    if (passeVrai != None) and (hashTable.hexdigest() == passeVrai[0]):
        cmd = 'SELECT * FROM Utilisateur WHERE courriel=' + courriel + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        info = cur.fetchone()

        global ProfileUtilisateur
        ProfileUtilisateur["courriel"] = courriel
        ProfileUtilisateur["nom"] = info[2]
        return render_template('bienvenu.html', profile=ProfileUtilisateur)

    return render_template('login.html', message="Informations invalides!")


@app.route("/signup")
def renderSignUpPage():
    return render_template('signup.html')


@app.route("/signup", methods=['POST'])
def signup():

    courriel = "'" + request.form.get('courriel') + "'"
    if ("@" not in courriel):
        return render_template('signup.html', message="Courriel invalide")

    password = request.form.get('motpasse')
    hashTable = hashlib.new('ripemd160')
    hashTable.update(password.encode('utf-8'))



    nom = "'" + request.form.get('nom') + "'"

    conn = pymysql.connect(host='localhost', user='root', password='root', db='testdb')
    cmd = 'INSERT INTO Utilisateur(courriel, motpasse, nom) VALUES('+courriel+','+ "'" + hashTable.hexdigest() + "'" +','+nom+');'
    cur = conn.cursor()
    try:
        cur.execute(cmd)
    except pymysql.err.IntegrityError:
        return render_template('signup.html', message="Ce courriel est déjà utilisé.")
    conn.commit()
    conn.close()
    return render_template('login.html')


@app.route("/decks")
def renderDeckPage():
    return render_template('decks.html')


@app.route("/catalog")
def get_cards():
    global card_names
    global image_sources

    card_names = []
    image_sources = []

    conn = pymysql.connect(host='localhost', user='root', password='root', db='testdb')
    cmd = 'SELECT * FROM cards' + ';'
    cur = conn.cursor()
    cur.execute(cmd)

    data = cur.fetchall()

    for d in data:
        card_names.append(d[0])
        image_sources.append(d[4])

    return render_template('catalog.html', card_info=list(data), image_sources=image_sources)


@app.route("/catalog", methods=['POST'])
def addSelectedCard():
    cardName = request.form.get('cardName')

    conn = pymysql.connect(host='localhost', user='root', password='kroot', db='testdb')
    cmd = 'SELECT * FROM Cards WHERE name=' + "'" + cardName + "'" + ";"
    cur = conn.cursor()
    if cur.execute(cmd) == 0:
        return render_template('catalog.html', names=card_names, image_sources=image_sources, message="This card is not in the catalog")
    selectedCards.append(cardName)
    conn.close()
    return render_template('catalog.html', names=card_names, image_sources=image_sources, message="The card was added to your Selection")


@app.route("/card_details/<card>", methods=['POST'])
def card_details(card):
    card_image = request.form.get('card-image')
    card_name = request.form.get('name')
    mana_cost = request.form.get('mana-cost')
    rarity = request.form.get('rarity')
    card_type = request.form.get('type')
    card_price = getCardPrice(card_name)
    card_instock = getCardInstock(card_name)


    return render_template('cardDetails.html', cardDetails=[card, mana_cost, rarity, card_type, card_image, card_price, card_instock])

def getCardPrice(cardName):
    conn = pymysql.connect(host='localhost', user='root', password='root', db='testdb')
    cmd = 'SELECT * FROM Catalog WHERE name=' + "'" + cardName + "'" + ";"
    cur = conn.cursor()
    cur.execute(cmd)

    return cur.fetchall()

def getCardInstock(cardName):
    conn = pymysql.connect(host='localhost', user='root', password='root', db='testdb')
    cmd = 'SELECT * FROM Contenir WHERE name=' + "'" + cardName + "'" + ";"
    cur = conn.cursor()
    cur.execute(cmd)

    return cur.fetchall()

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

    conn = pymysql.connect(host='localhost', user='root', password='root', db='testdb')
    cmd = 'SELECT * FROM cards NATURAL JOIN card_colors'

    if name_query != '"%%"':
        cmd = cmd + ' WHERE name LIKE {} '.format(name_query)

        if rarity != '""':
            cmd = cmd + 'AND rarity={} '.format(rarity)

            if card_type != '""':
                cmd = cmd + 'AND type={} '.format(card_type)

                if len(colors) > 1:
                    cmd = cmd + 'AND color IN {}'.format(colors) + ';'
                if len(colors) == 1:
                    cmd = cmd + 'AND color={}'.format('"' + colors[0] + '"') + ';'
            else:
                if len(colors) > 1:
                    cmd = cmd + 'AND color IN {}'.format(colors) + ';'
                if len(colors) == 1:
                    cmd = cmd + 'AND color={}'.format('"' + colors[0] + '"') + ';'
        else:
            if card_type != '""':
                cmd = cmd + 'AND type={}'.format(card_type)

                if len(colors) > 1:
                    cmd = cmd + 'AND color IN {}'.format(colors) + ';'
                if len(colors) == 1:
                    cmd = cmd + 'AND color={}'.format('"' + colors[0] + '"') + ';'
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

                if len(colors) > 1:
                    cmd = cmd + 'AND color IN {}'.format(colors) + ';'
                if len(colors) == 1:
                    cmd = cmd + 'AND color={}'.format('"' + colors[0] + '"') + ';'
            else:
                if len(colors) > 1:
                    cmd = cmd + 'AND color IN {}'.format(colors) + ';'
                if len(colors) == 1:
                    cmd = cmd + 'AND color={}'.format('"' + colors[0] + '"') + ';'
        else:
            if card_type != '""':
                cmd = cmd + ' WHERE type={}'.format(card_type)

                if len(colors) > 1:
                    cmd = cmd + 'AND color IN {}'.format(colors) + ';'
                if len(colors) == 1:
                    cmd = cmd + 'AND color={}'.format('"' + colors[0] + '"') + ';'
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


if __name__ == "__main__":
    app.run()
