import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
import os

class RecommenderSystem:
    def __init__(self):
        movies_path = os.path.join("data", "movies.csv")
        ratings_path = os.path.join("data", "ratings.csv")

        if not os.path.exists(movies_path):
            raise FileNotFoundError("movies.csv not found in data/ directory!")
        if not os.path.exists(ratings_path):
            raise FileNotFoundError("ratings.csv not found in data/ directory!")

        self.movies = pd.read_csv(movies_path)
        self.ratings = pd.read_csv(ratings_path)

        self.user_movie_matrix = None
        self.movie_id_to_index = None
        self.index_to_movie_id = None
        self.svd_matrix = None

        self.train_model()

    def train_model(self):
        self.user_movie_matrix = self.ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

        svd = TruncatedSVD(n_components=20)
        self.svd_matrix = svd.fit_transform(self.user_movie_matrix.T)

        self.movie_id_to_index = {movie_id: idx for idx, movie_id in enumerate(self.user_movie_matrix.columns)}
        self.index_to_movie_id = {idx: movie_id for movie_id, idx in self.movie_id_to_index.items()}

    def recommend(self, movie_title, top_n=5):
        movie_title = movie_title.strip().lower()
        match = self.movies[self.movies['title'].str.lower() == movie_title]

        if match.empty:
            return {"error": f"Movie '{movie_title}' not found!"}

        movie_id = int(match.iloc[0]['movieId'])

        if movie_id not in self.movie_id_to_index:
            return {"error": f"Movie ID {movie_id} not in rating matrix!"}

        idx = self.movie_id_to_index[movie_id]
        movie_vec = self.svd_matrix[idx].reshape(1, -1)
        similarity = cosine_similarity(movie_vec, self.svd_matrix)[0]

        similar_indices = similarity.argsort()[-top_n-1:-1][::-1]
        recommended_ids = [self.index_to_movie_id[i] for i in similar_indices]
        recommended_movies = self.movies[self.movies['movieId'].isin(recommended_ids)]

        return recommended_movies[['movieId', 'title']].to_dict(orient='records')
