import flask
from flask import jsonify, request
from flask_bcrypt import generate_password_hash

from db import db
from users import Users, user_schema, users_schema
from bid_items import BidItems


def add_user(req:flask.Request) -> flask.Response:
    post_data = request.json
    first_name = post_data.get('first_name')
    last_name = post_data.get('last_name')
    phone = post_data.get('phone')
    email = post_data.get('email')
    password = post_data.get('password')
    active = post_data.get('active')
    
    hashed_password = generate_password_hash(password).decode('utf8')
    record = Users(first_name, last_name, phone, email, hashed_password, active)

    db.session.add(record)
    db.session.commit()

    return jsonify(user_schema.dump(record)), 201


def get_all_active_users(req:flask.Request):
    all_users = db.session.query(Users).filter(Users.active == True).all()

    return jsonify(users_schema.dump(all_users)), 201

def update_user(req:flask.Request, user_id):
    post_data = request.json
    
    item_id = post_data.get('item_id')

    user_data = db.session.query(Users).filter(Users.user_id == user_id).first()
    record = db.session.query(BidItems).filter(BidItems.item_id == item_id).first()

    if (user_data == None) :
        return jsonify('Could not find user'), 404
    
    user_data.items.append(record)
    
    db.session.commit()

    return jsonify(user_schema.dump(user_data)), 201



    