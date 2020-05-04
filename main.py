from flask import Flask, render_template, request
import pymysql, pymysql.cursors
import uuid
import hashlib

app = Flask(__name__)
ProfileUtilisateur = {}

motDePasseDeLaDB = "mtgserver"

#For catalog
card_names = []
image_sources = []

selectedCards = []

#For user
followingCount = 0


@app.route("/")
def main():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def login():
    courriel = '"' + request.form.get('courriel') + '"'
    passe = request.form.get('motpasse')
    hashTable = hashlib.new('ripemd160')
    hashTable.update(passe.encode('utf-8'))


    conn= pymysql.connect(host='localhost',user='root', password=motDePasseDeLaDB ,db='testdb')
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
        nom = getName(courriel)
        balance = getBalance(courriel)
        followerCount = getFollowing(courriel)
        return render_template('user.html', ownership=True, userMail=request.form.get('courriel'), nom=nom, balance=balance, followerCount=followerCount)

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

    conn = pymysql.connect(host='localhost', user='root', password=motDePasseDeLaDB, db='testdb')
    cmd = 'INSERT INTO Utilisateur(courriel, motpasse, nom) VALUES('+courriel+','+ "'" + hashTable.hexdigest() + "'" +','+nom+');'
    cur = conn.cursor()
    try:
        cur.execute(cmd)
    except pymysql.err.IntegrityError:
        return render_template('signup.html', message="Ce courriel est déjà utilisé.")
    conn.commit()
    conn.close()
    return render_template('login.html')


@app.route("/user/<userMail>")
def renderDeckPage(userMail):
    ownership = False
    if "courriel" in ProfileUtilisateur.keys():
        if ('"' + userMail + '"') == ProfileUtilisateur["courriel"]:
            ownership = True
    return render_template('user.html', ownership=ownership, userMail=userMail)

@app.route("/user")
def createUserPage():
    userConnected = False
    userMail = None
    nom = None
    balance = None
    followerCount = None
    if "courriel" in ProfileUtilisateur.keys() and ProfileUtilisateur["courriel"] != None:
        userConnected = True
        userMail = ProfileUtilisateur["courriel"]
        nom = getName(userMail)
        balance = getBalance(userMail)
        followerCount = getFollowing(userMail)
    return render_template('user.html', ownership=True, userMail=userMail, nom=nom, balance=balance, followerCount=followerCount, userConnected=userConnected)

@app.route("/user", methods=['POST'])
def follow():
    searchedUser = request.form.get('searchedUser')
    ownership = False
    userMail = None
    nom = None
    balance = None
    followerCount = None
    message = None
    if "courriel" in ProfileUtilisateur.keys() and ProfileUtilisateur["courriel"] != None:
        ownership = True
        userMail = ProfileUtilisateur["courriel"]
        nom = getName(userMail)
        balance = getBalance(userMail)
        followerCount = getFollowing(userMail)

    result = followUser(userMail, searchedUser)

    if result:
        message = "Utilisateur suivi avec succès!"
    else:
        message = "Utilisateur est déjà suivi ou n'existe pas."

    return render_template('user.html', message=message, ownership=ownership, userMail=userMail, nom=nom, balance=balance, followerCount=followerCount)

@app.route("/user/<userMail>/decks")
def getUserDecks(userMail):
    ownership = False
    if "courriel" in ProfileUtilisateur.keys():
        if ('"' + userMail + '"') == ProfileUtilisateur["courriel"]:
            ownership = True

    conn = pymysql.connect(host='localhost', user='root', password=motDePasseDeLaDB, db='testdb')
    cmd = 'Select nom, D.deckId FROM Decks D INNER JOIN Deck_Owners D_O ON D.deckId = D_O.deckId WHERE owner_email = '+'"'+userMail+'"'+ "ORDER BY nom ;"
    cur = conn.cursor()
    cur.execute(cmd)

    userDecks = cur.fetchall()

    return render_template('userDecks.html', ownership=ownership, userMail=userMail, userDeckList=userDecks)


@app.route("/user/<userMail>/decks", methods=['POST'])
def createNewDeck(userMail):
    deckId = '"'+str(uuid.uuid4())+'"'
    deckName = '"'+request.form.get('deckName')+'"'

    ownerMail = '"'+userMail+'"'

    insertDeckCmd = "INSERT INTO Decks VALUES ("+deckId+','+deckName+');'
    insertDeckOwnerShipCmd = "INSERT INTO Deck_Owners VALUES ("+deckId+','+ownerMail+');'

    conn = pymysql.connect(host='localhost', user='root', password=motDePasseDeLaDB, db='testdb')
    cur = conn.cursor()
    cur.execute(insertDeckCmd)
    cur.execute(insertDeckOwnerShipCmd)
    conn.commit()
    conn.close()

    return getUserDecks(userMail)

@app.route("/catalog")
def get_cards():
    print('/catalog')
    global card_names
    global image_sources

    card_names = []
    image_sources = []

    conn = pymysql.connect(host='localhost', user='root', password=motDePasseDeLaDB, db='testdb')
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

    conn = pymysql.connect(host='localhost', user='root', password=motDePasseDeLaDB, db='testdb')
    cmd = 'SELECT * FROM Cards WHERE name=' + "'" + cardName + "'" + ";"
    cur = conn.cursor()
    if cur.execute(cmd) == 0:
        return render_template('catalog.html', names=card_names, image_sources=image_sources, message="This card is not in the catalog")
    selectedCards.append(cardName)
    conn.close()
    return render_template('catalog.html', names=card_names, image_sources=image_sources, message="The card was added to your Selection")


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

    conn = pymysql.connect(host='localhost', user='root', password=motDePasseDeLaDB, db='testdb')
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

def getFollowing(connected_user):
    conn = pymysql.connect(host='localhost', user='root', password=motDePasseDeLaDB, db='testdb')
    cmd = 'SELECT COUNT(email_followed_user) FROM Suivre WHERE email_user =' + connected_user + ';'
    cur = conn.cursor()
    cur.execute(cmd)
    return cur.fetchone()[0]

def getName(connected_user):
    conn = pymysql.connect(host='localhost', user='root', password=motDePasseDeLaDB, db='testdb')
    cmd = 'SELECT nom FROM Utilisateur WHERE courriel = ' + connected_user + ';'
    cur = conn.cursor()
    cur.execute(cmd)
    return cur.fetchone()[0]

def getBalance(connected_user):
    conn = pymysql.connect(host='localhost', user='root', password=motDePasseDeLaDB, db='testdb')
    cmd = 'SELECT balance FROM Utilisateur WHERE courriel = ' + connected_user + ';'
    cur = conn.cursor()
    cur.execute(cmd)
    return cur.fetchone()[0]

def followUser(connected_user, following_user):
    print(connected_user, following_user)
    conn = pymysql.connect(host='localhost', user='root', password=motDePasseDeLaDB, db='testdb')
    cmd = 'INSERT INTO Suivre(email_user, email_followed_user) VALUES(' + connected_user + ',\'' + following_user + '\');'
    cur = conn.cursor()
    try:
        cur.execute(cmd)
        conn.commit()
        conn.close()
        return True
    except pymysql.err.IntegrityError:
        conn.commit()
        conn.close()
        return False


@app.route("/card_details/<card>", methods=['POST'])
def card_details(card):
    card_image = request.form.get('card-image')
    card_name = request.form.get('name')
    mana_cost = request.form.get('mana-cost')
    rarity = request.form.get('rarity')
    card_type = request.form.get('type')

    return render_template('cardDetails.html', cardDetails=[card, mana_cost, rarity, card_type, card_image])


if __name__ == "__main__":
    app.run()
