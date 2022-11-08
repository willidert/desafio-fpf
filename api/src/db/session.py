# import os
# from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# load_dotenv()

# DB = os.getenv('POSTGRES_DB')
# PASSWORD = os.getenv('POSTGRES_PASSWORD')
# USER = os.getenv('POSTGRES_USER')
# SERVER = os.getenv('POSTGRES_SERVER')

# SQLALCHEMY_DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{SERVER}/{DB}'

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)