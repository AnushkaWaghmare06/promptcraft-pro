# backend/create_tables.py
from app.database import engine, Base
from app.models import user, project  # ensure models package imports exist

def create():
    Base.metadata.create_all(bind=engine)
    print("Tables created")

if __name__ == "__main__":
    create()
