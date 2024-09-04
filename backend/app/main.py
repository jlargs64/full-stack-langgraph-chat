from app.router.agent import router as agents_router
from app.router.user import router as users_router
from fastapi import FastAPI

# Uncomment if using Alembic for migrations
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=agents_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI with LangGraph example"}
