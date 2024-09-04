import logging
from contextlib import asynccontextmanager

from app.core.database import Base, SessionLocal
from app.core.settings import get_settings
from app.router.agent import router as agents_router
from app.router.user import router as users_router
from app.scripts.seed_db import seed_users
from app.services.user_service import get_user_service
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

settings = get_settings()
ENV = settings.env
DATABASE_URL = settings.database_url
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    user_service = get_user_service(db)
    # Seed users if dev
    if ENV == "dev":
        try:
            seed_users(db=db, user_service=user_service)
            logging.info("Test users seeded.")
        finally:
            db.close()
    yield
    # Clean up


app = FastAPI(lifespan=lifespan)

app.include_router(router=agents_router)
app.include_router(router=users_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI with LangGraph example"}


logging.info(f"API Running in {ENV} mode")
