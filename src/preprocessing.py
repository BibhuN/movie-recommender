# src/preprocessing.py
"""
This file cleans and prepares movie data for recommendations
"""

import os
import pandas as pd

class DataPreprocessor:
    """
    A class that prepares movie data for recommendations
    """
    
    def __init__(self):
        """
        Initialize - load the raw data
        """
        print("Loading data...")
        self.movies = pd.read_csv('data/movies.csv')
        self.ratings = pd.read_csv('data/ratings.csv')
        print(f"Loaded {len(self.movies)} movies")
        print(f"Loaded {len(self.ratings)} ratings")
    
    def clean_data(self):
        """
        Clean the movie titles - remove year from title
        """
        print("\nCleaning data...")

        # Extract year from title
        self.movies['year'] = self.movies['title'].str.extract(r'\((\d{4})\)')
        self.movies['year'] = pd.to_numeric(self.movies['year'], errors='coerce')

        # Remove year from title to get clean title
        self.movies['clean_title'] = self.movies['title'].str.replace(r'\s*\(\d{4}\)', '', regex=True)

        print("Extracted years from titles")
        print("Created clean titles")

        # Show example
        print("\nExample:")
        print(f"Original: {self.movies['title'].iloc[0]}")
        print(f"Clean: {self.movies['clean_title'].iloc[0]}")
        print(f"Year: {self.movies['year'].iloc[0]}")

        return self
    
    def prepare_features(self):
        """
        Prepare movie features for recommendation
        """
        print("\nPreparing features...")

        # Define keywords for tagging
        indian_keywords = ['dhurandhar', 'kgf', 'rrr', 'pushpa', 'gadar']

        # Combine genres, clean title, and add keyword tags
        self.movies['features'] = (
            self.movies['genres'].fillna('').str.replace('|', ' ') + ' ' +
            self.movies['clean_title'].fillna('') + ' ' +
            self.movies['clean_title'].fillna('').str.lower()
                .str.contains('|'.join(indian_keywords))
                .map({True: 'indian', False: ''})
        )

        print("Prepared combined features including genres, title, and tags")
        print("\nExample:")
        print(f"Original genres: {self.movies['genres'].iloc[0]}")
        print(f"Clean title: {self.movies['clean_title'].iloc[0]}")
        print(f"Prepared features: {self.movies['features'].iloc[0]}")

        return self
    
    def save_processed_data(self):
        """
        Save the cleaned data to a new CSV file
        """
        print("\nSaving processed data...")

        # Ensure data directory exists
        os.makedirs('data', exist_ok=True)
        self.movies.to_csv('data/movies_processed.csv', index=False)

        print("Saved to: data/movies_processed.csv")
        return self


# Main function - NO INDENTATION HERE!
if __name__ == "__main__":
    print("\n" + "="*60)
    print(" MOVIE DATA PREPROCESSING")
    print("="*60)
    
    # Create preprocessor object
    preprocessor = DataPreprocessor()
    
    # Run all the cleaning steps
    preprocessor.clean_data().prepare_features().save_processed_data()
    
    print("\n" + "="*60)
    print("PREPROCESSING COMPLETE!")
    print("="*60)
    
    # Show final result
    print(f"\nFinal dataset: {len(preprocessor.movies)} movies")
    print("\nSample of processed data:")
    print(preprocessor.movies[['clean_title', 'year', 'genres', 'features']].head())