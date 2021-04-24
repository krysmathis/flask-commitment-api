from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import time
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = 'commitment_users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    usertype = db.Column(db.Integer())
    latest_action_date = db.Column(db.DateTime())

    def __init__(self,username):
        self.username = username
    
    def __repr__(self):
        return "<User '{}'".format(self.username)

@app.route('/',methods=['GET','POST'])
def hello_world():
    template_data = {}
    return render_template('main.html', **template_data)

@app.route('/add', methods=['GET','POST'])
def add():
    print('add')
    json_data = request.json
    return json_data

if __name__ == "__main__":
    port = None
    app.run(host='0.0.0.0', port=5000,threaded=True)