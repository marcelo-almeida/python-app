from configuration.db_config import Database
from persistence.model import Category
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound


class CategoryRepository:

    def __init__(self):
        self.db = Database()

    def save(self, category: Category):
        session = self.db.session()
        try:
            session.add(category)
            session.commit()
        except SQLAlchemyError:
            session.rollback()
        finally:
            session.close()

    def delete(self, category: Category):
        session = self.db.session()
        try:
            session.delete(category)
            session.commit()
        except SQLAlchemyError:
            session.rollback()
        finally:
            session.close()

    def count(self) -> int:
        session = self.db.session()
        try:
            count = session.query(Category).count()
            return count
        except SQLAlchemyError:
            return 0
        finally:
            session.close()

    def get(self, limit=None, offset=None) -> list:
        session = self.db.session()
        try:
            if limit and offset:
                categories = session.query(Category).order_by(desc('name')).limit(limit).offset(offset)
            else:
                categories = session.query(Category).all()
            return categories
        except NoResultFound:
            return []
        finally:
            session.close()

    def get_by_id(self, category_id: int) -> Category:
        session = self.db.session()
        try:
            category = session.query(Category).filter_by(id=category_id).one()
            return category
        except NoResultFound:
            return None
        finally:
            session.close()

    def get_by_name(self, category_name: str) -> Category:
        session = self.db.session()
        try:
            category = session.query(Category).filter_by(name=category_name).one()
            return category
        except NoResultFound:
            return None
        finally:
            session.close()
