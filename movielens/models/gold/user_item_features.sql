-- what it does: builds a feature store for the recommendation model
-- Each row = one user-movie interaction with all features needed for ML
-- This is the direc input to the collaborative filtering model

with ratings as(
    select
    *
    from {{ref('stg_rating')}}
),

user_stats as (
    select
    *
    from {{ ref('user_activity')}}
),

movie_stats as (
    select
    *
    from {{ ref('movie_popularity')}}
),

joined as (
    select
    -- Keys
    r.user_id,
    r.movie_id,

    -- Target variable -- what the model will try to predict
    r.rating,

    -- User level Features
    u.rating_count as user_rating_count,
    u.average_rating as user_avg_rating,
    u.rating_range as user_rating_range,
    u.activity_date as user_active_days,

    --Movie level Features
    m.rating_count as movie_rating_count,
    m.average_rating as movie_avg_rating,
    m.unique_raters as movie_unique_raters,
    m.genres_raw as movie_genres,
    round(r.rating - u.average_rating, 2) as rating_vs_user_avg,

    --Temporal feature
    r.rate_timestamp as rate_timestamp
    from ratings r
    join user_stats u on r.user_id = u.user_id
    join movie_stats m on r.movie_id = m.movie_id
)

select
*
from 
joined