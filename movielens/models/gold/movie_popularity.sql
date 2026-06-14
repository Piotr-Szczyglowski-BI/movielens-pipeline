with ratings as (
    select
    * 
    from 
    {{ ref('stg_rating')}}
),

movies as (
    select
    *
    from
    {{ ref('stg_movie')}}
),

aggregated as (
    select
    r.movie_id,
    m.title,
    m.genres_raw,

    -- count of ratings
    count(r.rating) as rating_count,

    -- average rating
    avg(r.rating) as average_rating,

    -- min and max rating
    min(r.rating) as min_rating,
    max(r.rating) as max_rating,

    -- distinct count of users who rated the movie
    count(distinct r.user_id) as unique_raters

    from ratings r
    join movies m
    on r.movie_id = m.movie_id 
    group by
    r.movie_id,
    m.title,
    m.genres_raw,
)

select
*
from aggregated
order by rating_count desc
