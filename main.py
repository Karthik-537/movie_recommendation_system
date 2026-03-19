from fastapi import FastAPI
from apis.recommend_movies import router as recommend_router
from apis.register_user import router as user_router
from apis.login_user import router as auth_router

app = FastAPI()

app.include_router(recommend_router)
app.include_router(user_router)
app.include_router(auth_router)


