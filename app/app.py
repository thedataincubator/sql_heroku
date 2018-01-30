from flask import Flask, render_template, request, jsonify
from models import db, Person
import os 

app = Flask(__name__)

# Don't forget to export DATAbASE_URL must be an environment variable
# Heroku will do this automatically if we create use the postgres
# addon
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db.init_app(app)

@app.route('/age', methods=['POST'])
def get_age():
  age = request.form['age']
  people = Person.query.filter_by(age=age).all()
  html="".join(person.to_row() for person in people)
  return jsonify(html=html)
  
@app.route('/')
def index():
  people = Person.query.all()
  return render_template('index.html', people=people)

if __name__ == '__main__':
  app.run(port=33507)
