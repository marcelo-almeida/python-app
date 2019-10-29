from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = 'root'
DB_PASSWORD = 'root'
DB_ENDPOINT = 'localhost:3306/db'


class Database:

    def __init__(self):
        self.db_endpoint = self.get_db_endpoint()
        self.engine = create_engine(self.db_endpoint)

    def session(self):
        return sessionmaker(bind=self.engine)()

    @staticmethod
    def get_db_endpoint():
        return 'mysql+pymysql://{}:{}@{}'.format(DB_USER,
                                                 DB_PASSWORD,
                                                 DB_ENDPOINT)
