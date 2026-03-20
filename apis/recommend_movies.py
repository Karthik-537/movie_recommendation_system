from fastapi import APIRouter, Depends
import pandas as pd
import numpy as np
import pickle
from jwt.verify_jwt_token import verify_jwt_token

router = APIRouter(prefix="/movies")

model = pickle.load(open("artifacts/model.pkl", "rb"))
vectors = np.load("artifacts/vectors.npy")

df = pd.read_csv("data/movies.csv")


@router.get("/recommend")
def recommend(movie_name: str, k: int = 5, user=Depends(verify_jwt_token)):
    matches = df[df["title"].str.lower() == movie_name.lower()]
    if matches.empty:
        return {"Error": "Movie not found"}
    index = matches.index[0]
    distances, indices = model.kneighbors(
        vectors[index].reshape(1, -1),
        n_neighbors=k + 1
    )
    recommendations = []
    for i in indices[0][1:]:
        recommendations.append(df.iloc[i]["title"])
    return {
        "input_movie": movie_name,
        "recommendations": recommendations
    }


@router.get("/all")
def get_movies(user=Depends(verify_jwt_token)):
    return {
        "movies": list(df["title"])
    }
