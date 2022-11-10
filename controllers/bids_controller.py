import flask
from flask import jsonify, request

from db import db
from models.bids import Bids, BidsSchema

def set_bid(req:flask.Request) -> flask.Response:
    post_data = request.json

    user_id = post_data.get('user_id')
    item_id = post_data.get('item_id')
    bid_amount = post_data.get('bid_amount')

    exsisting_bid = db.session.query(Bids).filter(Bids.user_id == user_id).filter(Bids.item_id == item_id).first()
    
    if exsisting_bid:
        exsisting_bid.bid_amount = bid_amount
        db.session.commit()

        return jsonify('updated bid'), 200
      
    record = Bids(user_id, item_id, bid_amount)
    db.session.add(record)
    db.session.commit()

    return jsonify('added bid'), 200