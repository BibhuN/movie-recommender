# test_recommender.py
"""
Test and evaluate our recommendation system
"""

import pandas as pd
from src.content_based import ContentBasedRecommender

print("="*60)
print("TESTING MOVIE RECOMMENDER")
print("="*60)
 
 # Load recommender
print("\n Loading recommender...")
recommender = ContentBasedRecommender()
recommender.build_model()
print(" Recommender ready!")

# Test with different movies
print("\n" + "="*60)
print("TESTING WITH DIFFERENT MOVIES")
print("="*60)

test_movies = ["Toy Story", "Matrix", "Titanic"]

for movie in test_movies:
    print(f"\n--- Testing: {movie} ---")
    recommendations = recommender.get_recommendations(movie, n = 3)

    if recommendations:
        print(f"Top 3 recommendations:")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec['title']} (Similarity: {rec['similarity']:.3f})")
    else:
        print("No recommendations found")

# Metric 1: Coverage
print("\n" + "="*60)
print("METRIC 1: COVERAGE")  
print("Coverage = What % of movies can we recommend?")

total_movies = len(recommender.movies)
movies_with_features = len(recommender.movies[recommender.movies['features'].notna()])
coverage = (movies_with_features / total_movies) * 100

print(f"\n Total movies: {total_movies}")
print(f"Movies with features: {movies_with_features}")
print(f"Coverage: {coverage:.2f}%")

if coverage > 90:
    print("Excellent coverage!")
elif coverage > 70:
    print("Good coverage")
else:
    print("Coverage could be better")
            
# Metric 2: Diversity
print("\n" + "="*60)
print("METRIC 2: DIVERSITY")
print("="*60)
print("Diversity = Are recommendations from different genres?")

# Test diversity with one movie
test_movie = "Avatar"
recommendations = recommender.get_recommendations(test_movie, n=10)

if recommendations:
    # Extract all genres from recommendations
    all_genres = []
    for rec in recommendations:
        genres = rec['genres'].split('|')
        all_genres.extend(genres)

    # Count unique genres    
    unique_genres = set(all_genres)
    total_genre_mentions = len(all_genres)

    diversity_score = len(unique_genres) / total_genre_mentions

    print(f"\nTest movie: {test_movie}") 
    print(f"Total genre mentions: {total_genre_mentions}")
    print(f"Unique genres: {len(unique_genres)}")
    print(f"Genres found: {', '.join(sorted(unique_genres))}")
    print(f"Diversity score: {diversity_score:.3f}")

    if diversity_score > 0.5:
        print("High diversity - recommendations are varied!")
    elif diversity_score > 0.3:   
        print("Moderate diversity") 
    else:  
        print("Low diversity - recommendations are too similar") 
else:
    print(f"Movie '{test_movie}' not found")

# Metric 3: Popularity Bias
print("\n" + "="*60)
print("METRIC 3: POPULARITY BIAS")
print("="*60)
print("Popularity Bias = Do we only recommend famous movies?")

# Load ratings to check popularity
ratings = pd.read_csv('data/ratings.csv')

# Calculate how many ratings each movie has
movie_popularity = ratings.groupby('movieId').size().reset_index(name = 'num_ratings')

# Test with a movie 
test_movie = "Toy Story"
recommendations = recommender.get_recommendations(test_movie, n = 5)

if recommendations:
    print(f"\nTest movie: {test_movie}")
    print(f"Top 5 recommendations and their popularity:\n")

    popularity_scores = []

    for i, rec in enumerate(recommendations, 1):
        # Find movie ID
        movie_row = recommender.movies[recommender.movies['title'] == rec['title']]

        if not movie_row.empty:
            movie_id = movie_row.iloc[0]['movieId']

            # Get number of ratings 
            pop_data = movie_popularity[movie_popularity['movieId'] == movie_id]

            if not pop_data.empty:
                num_ratings = pop_data.iloc[0]['num_ratings']
                popularity_scores.append(num_ratings)
                print(f"{i}. {rec['title']}")
                print(f"   Ratings: {num_ratings}")
            else:
                print(f"{i}. {rec['title']}")
                print(f"   Ratings: 0 (no data)")

    if popularity_scores:
        avg_popularity = sum(popularity_scores) / len(popularity_scores) 
        print(f"\nAverage popularity: {avg_popularity:.1f} ratings")

        if avg_popularity > 100:
            print("High popularity bias - mostly recommending famous movies")
        elif avg_popularity > 50:
            print("Moderate popularity - good balance")
        else:
            print("Low popularity bias - recommernd hidden gems!")

    print("\n" + "="*60)
    print("EVALUATION COMPLETE!")
    print("="*60)                           
