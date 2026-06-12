-- File: stg_movies.sql
-- Description: This is a staging model for movies data from the MovieLens dataset. It prepares the raw data for further transformations and analysis.
-- Result: cleaned and structured movies data ready for downstream models.

with source as (
    select * from read_parquet('../data/bronze/movie.parquet')
),

renamed as (
    select
    movieId as movie_id,
    title as title,
    genres as genres_raw
    from source
)

select
*
from
renamed