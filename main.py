from flask import Flask, render_template, request
import pymysql, pymysql.cursors

app = Flask(__name__)
ProfileUtilisateur = {}

#For catalog
card_names = []
image_sources = []


@app.route("/")
def main():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def login():
    courriel = '"' + request.form.get('courriel') + '"'
    passe = request.form.get('motpasse')

    conn= pymysql.connect(host='localhost',user='root', password='mtgserver',db='testdb')
    cmd='SELECT motpasse FROM Utilisateur WHERE courriel='+courriel+';'
    cur=conn.cursor()

    cur.execute(cmd)
    passeVrai = cur.fetchone()

    if (passeVrai != None) and (passe == passeVrai[0]):
        cmd = 'SELECT * FROM Utilisateur WHERE courriel=' + courriel + ';'
        cur = conn.cursor()
        cur.execute(cmd)
        info = cur.fetchone()

        global ProfileUtilisateur
        ProfileUtilisateur["courriel"] = courriel
        print(info)
        ProfileUtilisateur["nom"] = info[2]
        return render_template('bienvenu.html', profile=ProfileUtilisateur)

    return render_template('login.html', message="Informations invalides!")


@app.route("/signup")
def renderSignUpPage():
    return render_template('signup.html')


@app.route("/signup", methods=['POST'])
def signup():

    courriel = '"' + request.form.get('courriel') + '"'
    if ("@" not in courriel):
        return render_template('signup.html', message="Courriel invalide")

    motpasse = '"' + request.form.get('motpasse') + '"'
    nom = '"' + request.form.get('nom') + '"'

    conn = pymysql.connect(host='localhost', user='root', password='mtgserver', db='testdb')
    cmd = 'INSERT INTO Utilisateur(courriel, motpasse, nom) VALUES('+courriel+','+motpasse+','+nom+');'
    cur = conn.cursor()
    try:
        cur.execute(cmd)
    except pymysql.err.IntegrityError:
        return render_template('signup.html', message="Ce courriel est déjà utilisé.")
    conn.commit()
    conn.close()
    return render_template('login.html')

@app.route("/catalog")
def get_cards():
    global card_names
    global image_sources

    card_names = []
    image_sources = []

    conn = pymysql.connect(host='localhost', user='root', password='mtgserver', db='testdb')
    cmd = 'SELECT * FROM cards' + ';'
    cur = conn.cursor()
    cur.execute(cmd)

    data = cur.fetchall()

    for d in data:
        card_names.append(d[0])
        image_sources.append(d[4])

    return render_template('catalog.html', names=card_names, image_sources=image_sources)

if __name__ == "__main__":
    app.run()