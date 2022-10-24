from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow

from db import db, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user@localhost:5000/biders'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app.db)

def create_all():
    with app.app_context()
      print('Creating tables...')
      db.create_all()
      print('All done')















if __name__ == '__main__':
    create_all()
    app.run(port=8089)