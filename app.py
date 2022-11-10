from flask import Flask, request, jsonify, Response, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from flask_bcrypt import generate_password_hash
from datetime import datetime, timedelta

from flask_bcrypt import Bcrypt
import uuid
from db import db, init_db
from flask_marshmallow import Marshmallow

from models.users import Users, user_schema, users_schema, UsersSchema
from models.bid_items import BidItems, BidItemsSchema, bid_item_schema, bid_items_schema
from models.categories import Categories, CategoriesSchema, category_schema, categories_schema
from models.bids import Bids, BidsSchema
from controllers import user_controller, categories_controller, bid_items_controller, bids_controller


import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user@localhost:5432/bidders'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)

def create_all():
    with app.app_context():
        print('Creating tables...')
        db.create_all()

        mock_category = db.session.query(Categories).filter(Categories.name == "Games").first()
        if not mock_category:
            name = 'Games'
            cat_descrip = "Items to bring the family and friends together. Try for lots of fun!"

            record = Categories(name, cat_descrip)

            db.session.add(record)
            db.session.commit()

        mock_item = db.session.query(BidItems).filter(BidItems.name == "Authentic Jenga").first()
        if not mock_item:
            
            category_data = db.session.query(Categories).filter(Categories.name == "Games").first()

            name = 'Authentic Jenga'
            description = 'Blocks game'
            base_price = 20.00
            category_id = category_data.category_id
            end_auction = datetime.utcnow() + timedelta(hours=200)

            record = BidItems(name, description, base_price, category_id, end_auction)
            db.session.add(record)
            db.session.commit()


            name = 'Authentic Uno'
            description = 'Card game to end friendships'
            base_price = 50.00
            category_id = category_data.category_id
            end_auction = datetime.utcnow() + timedelta(hours=200)

            record = BidItems(name, description, base_price, category_id, end_auction)
            db.session.add(record)
            db.session.commit()


            name = 'Authentic Monopoloy'
            description = 'Learn to rule the world'
            base_price = 1000000.00
            category_id = category_data.category_id
            end_auction = datetime.utcnow() + timedelta(hours=200)

            record = BidItems(name, description, base_price, category_id, end_auction)
            db.session.add(record)
            db.session.commit()

        mock_user = db.session.query(Users).filter(Users.email == "thefirstguysemail@email.com").first()

        if not mock_user:
            first_name = 'the First Guy'
            last_name = 'Dude'
            phone = '555-555-5555'
            email = 'thefirstguysemail@email.com'
            password = 'password1'
            active = True
            
            hashed_password = generate_password_hash(password).decode('utf8')
            record = Users(first_name, last_name, phone, email, hashed_password, active)

            db.session.add(record)
            db.session.commit()   

            first_name = 'I will buy'
            last_name = 'your cat'
            phone = '555-555-5555'
            email = 'catman@catacat.com'
            password = 'password2'
            active = True
            
            hashed_password = generate_password_hash(password).decode('utf8')
            record = Users(first_name, last_name, phone, email, hashed_password, active)

            db.session.add(record)
            db.session.commit() 

            first_name = 'John'
            last_name = 'Doe'
            phone = '555-555-5555'
            email = 'example@example.com'
            password = 'password3'
            active = True
            
            hashed_password = generate_password_hash(password).decode('utf8')
            record = Users(first_name, last_name, phone, email, hashed_password, active)

            db.session.add(record)
            db.session.commit()

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
    return bids_controller.set_bid(request)

if __name__ == '__main__':
    create_all()
    app.run(port=4000)