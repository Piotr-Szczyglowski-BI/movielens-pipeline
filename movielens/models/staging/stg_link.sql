-- standardize link table with IMDb and TMDb IDs

with source as (
    select * from read_parquet('../data/bronze/link.parquet')
),

renamed as (
    select
    movieId as movie_id,
    imdbId as imdb_id,
    tmdbId as tmdb_id
    from
    source
)

select
*
from
renamed