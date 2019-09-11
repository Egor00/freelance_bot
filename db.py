from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_models import base, User
from settings import DB_URI

db = create_engine(DB_URI)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)
