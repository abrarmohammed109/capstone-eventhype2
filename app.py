from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Hello123@localhost/eventHype'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFACTIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Person(db.Model):
    __tablename__ = 'person'
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
        if db.session.query(Person).filter(Person.userName == userName).count() == 0:
            data = Person(userName,comments)
            db.session.add(data)
            db.session.commit()
        return render_template('thanks.html')
    

if __name__ == '__main__':
    app.run()