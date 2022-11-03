import flask
from flask import jsonify, request

from db import db
from bid_items import BidItems, bid_item_schema, bid_items_schema


def add_bid_item(req:flask.Request) -> flask.Response:
    post_data = request.json
    name = post_data.get('name')
    description = post_data.get('description')
    base_price = post_data.get('base_price')
    category_id = post_data.get('category_id')
    end_auction = post_data.get('end_auction')
    
    record = BidItems(name, description, base_price, category_id, end_auction)

    db.session.add(record)
    db.session.commit()

    return jsonify(bid_item_schema.dump(record)), 200


def get_all_items(req:flask.Request):
    items = db.session.query(BidItems).all()

    return jsonify(bid_items_schema.dump(items)), 200