from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings

engine = create_engine(settings.db.driver, echo=True)
Session = sessionmaker(bind=engine)
