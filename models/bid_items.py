import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_marshmallow import Marshmallow
import marshmallow as ma
from datetime import datetime

from db import db
# from bids import BidsSchema


class BidItems(db.Model):
    __tablename__='BidItems'
    item_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    base_price = db.Column(db.Float())
    category_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Categories.category_id'))
    end_auction = db.Column(db.String())

    bid_info = db.relationship('Bids', back_populates = 'item')

    def __init__(self, name, description, base_price, category_id, end_auction):
        self.name = name
        self.description = description
        self.base_price = base_price
        self.category_id = category_id
        self.end_auction = end_auction

class BidItemsSchema(ma.Schema):
    class Meta:
        fields = ['item_id', 'name', 'description', 'base_price', 'category_id', 'end_auction', 'bid_info']

    bid_info = ma.fields.Nested('BidsSchema', many=True, exclude=['item'])

bid_item_schema = BidItemsSchema()
bid_items_schema = BidItemsSchema( many=True )