import flask
from flask import jsonify, request

from db import db
from categories import Categories, category_schema, categories_schema

# name, description, base_price, category_id, end_auction
def add_category(req:flask.Request) -> flask.Response:
    post_data = request.json
    name = post_data.get('name')
    cat_descrip = post_data.get('cat_descrip')
    
    record = Categories(name, cat_descrip)

    db.session.add(record)
    db.session.commit()

    return jsonify(category_schema.dump(record)), 201


# def get_all_categories(req:flask.Request):
#     all_users = db.session.query(Users).filter(Users.active == True).all()

#     return jsonify(users_schema.dump(all_users)), 201