import flask
import app
app = flask.Flask(__name__)

@app.route('/')
def pageMain():
  return flask.render_template('main.html')

@app.route('/login')
def pageLogin():
  return flask.render_template('login.html')

@app.route('/reg')
@app.route('/register')
def pageRegister():
  return flask.render_template('register.html')

if __name__ == '__main__':
  app.run(debug=True) 