with ratings as(
    select
    *
    from
    {{ref ("stg_rating")}}
),

aggregated as (
    select
    user_id,
    count(rating) as rating_count,
    round(avg(rating), 2) as average_rating,
    max(rating)-min(rating) as rating_range,
    min(rate_timestamp) as first_rating_timestamp,
    max(rate_timestamp) as last_rating_timestamp,
    date_diff('day',
        min(rate_timestamp),
        max(rate_timestamp)) as activity_date

from ratings
group by user_id
)

select 
*
from
aggregated
order by rating_count desc