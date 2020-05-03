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
        return render_template('user.html', ownership=True, userMail=request.form.get('courriel'))

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
    if ('"' + userMail + '"') == ProfileUtilisateur["courriel"]:
        ownership = True
    return render_template('user.html', ownership=ownership, userMail=userMail)


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

    return render_template('user.html', ownership=True, userMail=userMail)




@app.route("/catalog")
def get_cards():
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

    return render_template('catalog.html', names=card_names, image_sources=image_sources)


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

def get_following(connected_user):
    conn = pymysql.connect(host='localhost', user='root', password='motDePasseDeLaDB', db='testdb')
    cmd = 'SELECT COUNT(email_followed_user) FROM Suivre WHERE email_user =\'' + connected_user + '\';'
    cur = conn.cursor()
    cur.execute(cmd)
    following_users_count = cur.fetchone()
    print(following_users_count)

def follow_user(connected_user, following_user):
    print(connected_user)
    print(following_user)
    conn = pymysql.connect(host='localhost', user='root', password='motDePasseDeLaDB', db='testdb')
    cmd = 'INSERT INTO Suivre(email_user, email_followed_user) VALUES(\'' + connected_user + '\', \'' + following_user + '\');'
    cur = conn.cursor()
    try:
        cur.execute(cmd)
    except pymysql.err.IntegrityError:
        print('La personne est déjà suivi.')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    app.run()
