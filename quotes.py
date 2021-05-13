from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:postgres@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://zfsajbnahqpklj:5958da46f3c9824d4df784edc40af75434b43212eedc5287aedd71e7f92c7738@ec2-107-20-153-39.compute-1.amazonaws.com:5432/daa5kmtajit6qp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result=Favquotes.query.all()
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods=['POST'])
def process():
    author=request.form['author']
    quote=request.form['quote']
    quotedata=Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))

# Before running this file, open python console in venv and do:
# from quotes import db
# db.create_all()
