# db/scripts/create_db_mysql.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from app.config import settings
from db.models import Base
import os

# python -m db.scripts.create_db_mysql

base_dir = os.path.dirname(__file__)
main_db_path = os.path.join(base_dir, "..", "data", "main.db")
main_db_path = os.path.abspath(main_db_path)
main_db_url = f"sqlite:///{main_db_path}"

engine = create_engine(main_db_url)
Base.metadata.create_all(engine)


print(f"Created at {main_db_url}")
