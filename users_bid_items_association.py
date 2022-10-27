from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma

users_bid_items_association_table = db.Table(
    'UserBidItemAssociation',
    db.Model.metadata,
    db.Column('user_id', db.ForeignKey('Users.user_id'), primary_key=True),
    db.Column('item_id', db.ForeignKey('BidItems.item_id'), primary_key=True)

)

# class or variable - - for simple join
# Do class - if you want to store other info here as well. 