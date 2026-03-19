import pandas as pd
import numpy as np
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Step 1: Load dataset
df = pd.read_csv("data/movies.csv")
df = df.dropna()

# Step 2: Feature extraction
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df["features"])

# Step 3: Train KNN
model = NearestNeighbors(metric="cosine", algorithm="brute")
model.fit(vectors)

# Step 4: Save artifacts
os.makedirs("artifacts", exist_ok=True)

pickle.dump(model, open("artifacts/model.pkl", "wb"))
np.save("artifacts/vectors.npy", vectors.toarray())

print("Training complete. Artifacts saved.")