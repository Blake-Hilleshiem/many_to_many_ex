from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

from models.bid_items import BidItemsSchema

class Bids(db.Model):
    __tablename__='Bids'
    user_id = db.Column(UUID(as_uuid = True), db.ForeignKey('Users.user_id'), primary_key = True)
    item_id = db.Column(UUID(as_uuid = True), db.ForeignKey('BidItems.item_id'), primary_key = True)
    bid_amount = db.Column(db.Float())

    client = db.relationship('Users', back_populates = 'bid_info')
    item = db.relationship('BidItems', back_populates = 'bid_info')
    # user_bid = db.relationship('BidItems', back_populates = 'user_bid')

    def __init__(self, user_id, item_id, bid_amount):
        self.user_id = user_id      
        self.item_id = item_id      
        self.bid_amount = bid_amount

class BidsSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'item', 'bid_amount']
  
    
    item = ma.fields.Nested(BidItemsSchema())
    # user_bid = ma.fields.Nested(BidItemsSchema(), exclude=['item'])

bid_schema = BidsSchema()
bids_schema = BidsSchema( many=True )

    
