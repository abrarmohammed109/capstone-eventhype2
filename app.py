from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCEHMY_DATABASE_URI'] = 'postgresql://postgres:Hello123@localhost/eventHype'

else:
    app.debug = False
    app.config['SQLALCEHMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFACTIONS'] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(200), unique=True)
    comments = db.Column(db.Text())

def __init__(self, userName, comments):
    self.userName = userName
    self.comments = comments
    



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        userName = request.form['username']
        comments = request.form['comments']
        print(userName,comments)
        return render_template('thanks.html')
    

if __name__ == '__main__':
    app.run()