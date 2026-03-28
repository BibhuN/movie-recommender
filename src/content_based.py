# src/content_based.py
"""
Content-Based Recommendation System
Recommends movies based on genres
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    """
    Recommends movies similar to what you like
    """
    
    def __init__(self):
        """
        Load the processed data
        """
        print(" Loading processed data...")
        self.movies = pd.read_csv('data/movies_processed.csv')
        print(f" Loaded {len(self.movies)} movies")
    
    def build_model(self):
        """
        Convert movie features into numbers using TF-IDF
        Then calculate similarity between all movies
        """
        print("\n Building TF-IDF model...")
        
        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer()
        
        # Convert features to numbers
        self.tfidf_matrix = self.vectorizer.fit_transform(self.movies['features'])
        
        print(f" Converted {len(self.movies)} movies into vectors")
        print(f" Matrix shape: {self.tfidf_matrix.shape}")
        
        # Calculate similarity between all movies
        print("\n Calculating movie similarities...")
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)
        
        print(f" Similarity matrix created: {self.similarity_matrix.shape}")
        print(" Model ready!")
        
        return self
    
    def get_recommendations(self, movie_title, n=5):
        """
        Get movie recommendations based on a movie title
        
        movie_title: Name of the movie (example: "Toy Story")
        n: How many recommendations to return (default 5)
        """
        print(f"\n Finding movies similar to: {movie_title}")
        
        # Find the movie in our dataset
        matches = self.movies[self.movies['clean_title'].str.contains(movie_title, case=False, na=False)]
        
        if len(matches) == 0:
            print(f"Movie '{movie_title}' not found!")
            return None
        
        # Get the first match
        movie_idx = matches.index[0]
        movie_name = self.movies.loc[movie_idx, 'title']
        
        print(f" Found: {movie_name}")
        
        # Get similarity scores for this movie
        similarity_scores = self.similarity_matrix[movie_idx]
        
        # Create a list of (movie_index, similarity_score) pairs
        movie_scores = list(enumerate(similarity_scores))
        
        # Sort by similarity score (highest first)
        movie_scores = sorted(movie_scores, key=lambda x: x[1], reverse=True)
        
        # Get top N movies (skip first one - it's the movie itself!)
        top_movies = movie_scores[1:n+1]
        
        # Get movie details
        recommendations = []
        for idx, score in top_movies:
            recommendations.append({
                'title': self.movies.loc[idx, 'title'],
                'genres': self.movies.loc[idx, 'genres'],
                'similarity': score
            })
        
        return recommendations

# Main function - runs when we execute this file
if __name__ == "__main__":
    print("\n" + "="*60)
    print(" CONTENT-BASED MOVIE RECOMMENDER")
    print("="*60)
    
    # Create recommender
    recommender = ContentBasedRecommender()
    
    # Build the model
    recommender.build_model()
    
    # Test with a movie
    print("\n" + "="*60)
    print(" TESTING RECOMMENDATIONS")
    print("="*60)
    
    # Get recommendations for "Toy Story"
    movie_name = "Toy Story"
    recommendations = recommender.get_recommendations(movie_name, n=5)
    
    # Display results
    if recommendations:
        print(f"\n Top 5 movies similar to '{movie_name}':\n")
        for i, movie in enumerate(recommendations, 1):
            print(f"{i}. {movie['title']}")
            print(f"   Genres: {movie['genres']}")
            print(f"   Similarity: {movie['similarity']:.3f}")
            print()
