from fastapi import FastAPI
from apis.recommend_movies import router as recommend_router
from apis.register_user import router as user_router

app = FastAPI()

app.include_router(recommend_router)
app.include_router(user_router)


