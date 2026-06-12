-- standardize tag table 

with source as (
    select * from read_parquet('../data/bronze/tag.parquet')
),

renamed as (
    select
    userId as user_id,
    movieId as movie_id,
    tag as tag,
    cast(timestamp as timestamp) as tag_timestamp
    from
    source
)

select
*
from
renamed