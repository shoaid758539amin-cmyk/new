from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL="postgresql+psycopg2://shoaid_user:pg5M0O08cGtiCqvX5TpCruGltKRinrdG@dpg-dc37rlou01pc73dr6h50-a.ohio-postgres.render.com/shoaid"
#DATABASE_URL = "postgresql+psycopg2://training_rn82_user:Dw0W65kwL8h1D2iyOBYEKBWJ2su56Ibk@dpg-dc35cq9ksfps7392o240-a.oregon-postgres.render.com/training_rn82"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()
