from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from configuration.db_config import Database

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500))
    price = Column(Float(precision=2))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', uselist=False, back_populates='product')

    @property
    def serialize(self):
        """Return object to JSON format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'cat_id': self.category_id
        }

    @property
    def serialize_with_category(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.serialize_one2one
        }

    @property
    def serialize_one2one(self):
        return self.category.serialize


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    product = relationship(Product)

    @property
    def serialize_with_item(self):
        """Return object to JSON format"""
        return {
            'name': self.name,
            'id': self.id,
            'item': self.serialize_one2many
        }

    @property
    def serialize(self):
        """Return object to JSON format"""
        return {
            'name': self.name,
            'id': self.id
        }

    @property
    def serialize_one2many(self):
        return [i.serialize for i in self.product]


if __name__ == '__main__':
    db = Database()
    Base.metadata.create_all(db.engine)
