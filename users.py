import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from users_bid_items_association import users_bid_items_association_table
from db import db
# from organizations import

class Users(db.Model):
    __tablename__='Users'
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String())
    phone = db.Column(db.String())
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String())
    active = db.Column(db.Boolean(), default=True)

    items = db.relationship('BidItems', secondary=users_bid_items_association_table, back_populates='clients')
    #                                                                                                ^^ virtual variable.
    
    def __init__(self,first_name,last_name,phone,email,password, active):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.active = active

class UsersSchema(ma.Schema):
    items = ma.fields.Nested('BidItemsSchema', many=True, exclude=['clients'])
    class Meta:
        fields = ['user_id','first_name','last_name','phone','email','password', 'active', 'items']




user_schema = UsersSchema()
users_schema = UsersSchema( many=True )
                    #           ^^ references returns a list of objects


    # items = db.relationship('bid_items', back_populates='', lazy=True )

    # <association name> = db.relationship(<class_name>,  back_populates=<class_name>)
    #                                                             ^^ a field

    # secondary='users_bid_items_association',