from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
import os 

app = Flask(__name__)
# Hack to get locally working when running create_db.py
try:
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
except KeyError:
  with open('.env', 'r') as fp:
    lines = fp.readlines()
  app_vars = {i.split('=')[0]:i.split('=')[1][1:-2] for i in lines}
  app.config['SQLALCHEMY_DATABASE_URI'] = app_vars['DATABASE_URL']

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)

@app.route('/')
def index():
  people = Person.query.all()
  return render_template('index.html', people=people)

if __name__ == '__main__':
  app.run(port=33507)
