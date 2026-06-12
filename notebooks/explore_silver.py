import duckdb as ddb

connection = ddb.connect(database="data/silver/movielens.duckdb", read_only = True)

print('== Objects in database ==')
print(connection.execute("SHOW ALL TABLES").df())

for model in ['stg_movie', 'stg_rating', 'stg_tag', 'stg_link']:
    print(f"\n== {model} (pierwsze 3 wiersze) ===")
    print(connection.execute(f"SELECT * FROM {model} LIMIT 3").df())


connection.close()