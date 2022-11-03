from flask import Flask, request, jsonify, Response, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

from flask_bcrypt import Bcrypt
import uuid
from db import db, init_db
from flask_marshmallow import Marshmallow

from users import Users, user_schema, users_schema, UsersSchema
from bid_items import BidItems, BidItemsSchema, bid_item_schema, bid_items_schema
from categories import Categories, CategoriesSchema, category_schema, categories_schema
from controllers import user_controller, categories_controller, bid_items_controller

from bids import Bids, BidsSchema


import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user@localhost:5432/bidders'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)

def create_all():
    with app.app_context():
      print('Creating tables...')
      db.create_all()
      print('All done')

@app.route('/user/add', methods=['POST'])
def add_user() -> Response:
    return user_controller.add_user(request)

@app.route('/user/get-all', methods=['GET'])
def get_all_active_users() -> Response:
    return user_controller.get_all_active_users(request)

@app.route('/category/add', methods=['POST'])
def add_category() -> Response:
    return categories_controller.add_category(request)

@app.route('/category/get-all', methods=['GET'])
def get_all_categories() -> Response:
    return categories_controller.get_all_categories(request)

@app.route('/bid-item/add', methods=['POST'])
def add_item() -> Response:
    return bid_items_controller.add_bid_item(request)

@app.route('/user/update/<user_id>', methods=['PUT'])
def update_user(user_id) -> Response:
    return user_controller.update_user(request, user_id)

@app.route('/bid-item/get-all', methods=['GET'])
def get_all_items():
    return bid_items_controller.get_all_items(request)


@app.route('/set-bid', methods = ['POST'])
def set_bid():
    post_data = request.json

    user_id = post_data.get('user_id')
    item_id = post_data.get('item_id')
    bid_amount = post_data.get('bid_amount')
    
    record = Bids(user_id, item_id, bid_amount)
    db.session.add(record)
    db.session.commit()

    return jsonify('added bid'), 200


if __name__ == '__main__':
    create_all()
    app.run(port=4000)