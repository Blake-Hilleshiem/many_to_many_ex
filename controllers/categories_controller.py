import flask
from flask import jsonify, request

from db import db
from categories import Categories, category_schema, categories_schema


def add_category(req:flask.Request) -> flask.Response:
    post_data = request.json
    name = post_data.get('name')
    cat_descrip = post_data.get('cat_descrip')
    
    record = Categories(name, cat_descrip)

    db.session.add(record)
    db.session.commit()

    return jsonify(category_schema.dump(record)), 200


def get_all_categories(req:flask.Request):
    all_categories = db.session.query(Categories).all()

    return jsonify(categories_schema.dump(all_categories)), 201