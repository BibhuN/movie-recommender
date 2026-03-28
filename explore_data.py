#explore_data.py
import pandas as pd
print("="*50)
print("MOVIE RECOMMENDATION SYSTEM - DATA EXPLORATION")
print("="*50)
print("\n Loading data...")
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')
print("Data loaded successfully!")
print(f"Movies:{len(movies)} rows")
print(f"Ratings:{len(ratings)} rows")
# Let's see what the movies data looks like
print("\n" + "=" * 50)
print("MOVIES DATA - First 5 Rows")
print("=" * 50)
print(movies.head())
print("\n" + "=" * 50)
print("RATINGS DATA - First 5 Rows")
print("=" * 50)
print(ratings.head())
# Let's see what columns we have
print("\n" + "=" * 50)
print("Movies Columns:")
print("=" * 50)
print(movies.columns.tolist())
print("\n Ratings Columns:")
print(ratings.columns.tolist())

import pandas as pd

print("=" * 50)
print("MOVIE RECOMMENDATION SYSTEM - DATA EXPLORATION")
print("=" * 50)

# Load data
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

print("\nData loaded successfully!")
print(f"Movies: {len(movies)} rows")
print(f"Ratings: {len(ratings)} rows")

print("\n" + "=" * 50)
print("LAST 15 MOVIES (CHECK YOUR ADDED DATA)")
print("=" * 50)
print(movies.tail(15))