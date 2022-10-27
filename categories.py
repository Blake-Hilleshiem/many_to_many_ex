import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db

class Categories(db.Model):
    __tablename__='Categories'
    
    category_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String())
    cat_descrip = db.Column(db.String())

    def __init__(self, name,  cat_descrip):
        self.name = name
        self.cat_descrip = cat_descrip

class CategoriesSchema(ma.Schema):
    class Meta:
        fields = ['name', 'category_id', 'cat_descrip']

category_schema = CategoriesSchema()
categories_schema = CategoriesSchema( many=True )