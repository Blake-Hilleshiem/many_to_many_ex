import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_marshmallow import Marshmallow
import marshmallow as ma
from datetime import datetime

# from users_bid_items_association import users_bid_items_association_table
from db import db

class BidItems(db.Model):
    __tablename__='BidItems'
    item_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    base_price = db.Column(db.Float())
    # category_id = db.relationship('Category', backref='Bid_items', lazy=True)
    # category_id = db.Column(UUID(as_uuid=True), ForeignKey=True)
    end_auction = db.Column(db.String())

    # category = db.relationship('', back_populates = 'items')
    bid_info = db.relationship('Bids', back_populates = 'items')

    def __init__(self, name, description, base_price, category_id, end_auction):
        self.name = name
        self.description = description
        self.base_price = base_price
        self.category_id = category_id
        self.end_auction = end_auction

class BidItemsSchema(ma.Schema):
    class Meta:
        fields = ['item_id', 'name', 'description', 'base_price', 'category_id', 'end_auction', 'bid_info']

    bid_info = ma.fields.Nested('BidsSchema', many=True, exclude=['item_id'])

bid_item_schema = BidItemsSchema()
bid_items_schema = BidItemsSchema( many=True )





