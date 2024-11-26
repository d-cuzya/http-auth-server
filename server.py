import flask
import app
import hashlib
import json
import psycopg2

app = flask.Flask(__name__)
with open('./settings.json', 'r') as file:
    settings = json.load(file)
dbconn = psycopg2.connect(dbname=settings["database"]["dbname"], user=settings["database"]["user"], password=settings["database"]["password"], host=settings["database"]["host"])
cursor = dbconn.cursor()

@app.route('/')
def pageMain():
  return flask.render_template('main.html')

@app.route('/login', methods=['GET'])
def pageLogin():
  return flask.render_template('login.html', error="")

@app.route('/login', methods=['POST'])
def postLogin():
  print("POST")
  email = flask.request.form.get("email")
  sha256_hash = hashlib.sha256()
  sha256_hash.update(flask.request.form.get("password").encode())
  password = sha256_hash.hexdigest()
  cursor.execute(f"SELECT EXISTS(SELECT email, password FROM users WHERE email = '{email}' AND password = '{password}' LIMIT 1);")
  if cursor.fetchone()[0] == True:
    return flask.redirect("/")
  else:
    return flask.render_template('login.html', error="Логин или пароль содержит ошибку!")

@app.route('/register', methods=['GET'])
def pageRegister():
  return flask.render_template('register.html', error="")

@app.route('/register', methods=['POST'])
def postRegister():
  email = flask.request.form.get("email")
  sha256_hash = hashlib.sha256()
  sha256_hash.update(flask.request.form.get("password").encode())
  password = sha256_hash.hexdigest()
  cursor.execute(f"SELECT EXISTS(SELECT email FROM users WHERE email='{email}' LIMIT 1)")
  if not cursor.fetchone()[0] == True:
    cursor.execute(f"INSERT INTO users (email, password) VALUES ('{email}', '{password}');")
    dbconn.commit()
    return app.redirect("/")
  else:
    return flask.render_template('register.html', error="Пользователь с этой почтой уже существует!")

if __name__ == '__main__':
  app.run(debug=True) 