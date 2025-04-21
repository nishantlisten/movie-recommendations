from flask import Flask, jsonify, request
from model.recommender import RecommenderSystem

app = Flask(__name__)
recommender = RecommenderSystem()

@app.route('/')
def index():
    return '🎬 Welcome to the Movie Recommendation API! Use POST /recommend with {"title": "Movie Title"}'

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    try:
        data = request.get_json()
        if not data or "title" not in data:
            return jsonify({"error": "Missing 'title' in request body"}), 400

        title = data["title"]
        recommendations = recommender.recommend(title)

        return jsonify(recommendations)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
