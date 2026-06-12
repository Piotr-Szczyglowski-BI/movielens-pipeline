-- Description: Standardize rating table from movielens dataset. 
-- converts timestamp unix to datetime

with source as (
    select * from read_parquet('../data/bronze/rating.parquet')
),

renamed as (
    select
    userId as user_id,
    movieId as movie_id,
    rating as rating,
    to_timestamp(cast(timestamp as bigint)) as rate_timestamp
    from source
)

select 
*
from
renamed