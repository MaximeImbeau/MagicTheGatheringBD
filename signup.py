from flask import Flask, render_template, request
import pymysql, pymysql.cursors

app = Flask(__name__)

@app.route("/")
def main():
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

if __name__ == "__main__":
    app.run()