from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_ENDPOINT = 'localhost:5432/db'


class Database:

    def __init__(self):
        self.db_endpoint = self.get_db_endpoint()
        self.engine = create_engine(self.db_endpoint)

    def session(self):
        return sessionmaker(bind=self.engine)()

    @staticmethod
    def get_db_endpoint():
        return 'postgresql+psycopg2://{}:{}@{}'.format(DB_USER,
                                                       DB_PASSWORD,
                                                       DB_ENDPOINT)
