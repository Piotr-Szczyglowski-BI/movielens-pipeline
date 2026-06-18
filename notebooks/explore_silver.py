import duckdb as ddb

# Connect to the DuckDB database created by dbt (read-only to avoid accidental writes)
connection = ddb.connect(database="data/silver/movielens.duckdb", read_only=True)

# Show all tables and views in the database
print("=== Objects in database ===")
print(connection.execute("SHOW ALL TABLES").df())

# Preview first 3 rows of each staging model
for model in ["stg_movie", "stg_rating", "stg_tag", "stg_link"]:
    print(f"\n=== {model} (first 3 rows) ===")
    print(connection.execute(f"SELECT * FROM {model} LIMIT 3").df())

# Top 5 most popular movies by rating count
print("\n=== movie_popularity (top 5 movies) ===")
print(connection.execute("SELECT * FROM movie_popularity LIMIT 5").df())

# Top 5 most active users by number of ratings
print("\n=== user_activity (top 5 users) ===")
print(connection.execute("SELECT * FROM user_activity LIMIT 5").df())

# Top 5 rows ofr user_item_features table
print("\n=== user_item_features (top 5 rows) ===")
print(connection.execute("SELECT * FROM user_item_features LIMIT 5").df())

# Count of records of user_item_features table
print("\n== Count of records in user_item_Featues table ===")
print(connection.execute("SELECT COUNT(*) FROM user_item_features").df())

connection.close()