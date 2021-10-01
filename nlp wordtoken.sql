select distinct(word), count(word) as ranking
from wordtoken
group by word
order by ranking desc
limit 10;

delete from wordtoken;