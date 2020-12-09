Samantha Michelle Garcia

DSNY Salt Usage

#Queries & Results

#Table Name- salt

#Table Design

Columns

Primary Key- surrogate key, serial
stormnumber- integer, identifies which storm in a given year it is
date- timestamptz
manhattan, bronx, brooklyn, queens, statenisland, total tons- integer, tons of salt used

#Tables in database

\dt



           List of relations
 Schema | Name | Type  |     Owner      
--------+------+-------+----------------
 public | salt | table | samanthagarcia
(1 row)


#01- total number of rows in the table

SELECT COUNT(*)
FROM salt;


 count
-------
   106
(1 row)


#02- adding a new column without a default value

ALTER TABLE salt
ADD COLUMN average int;


                               Table "public.salt"
    Column    |  Type   | Collation | Nullable |             Default              
--------------+---------+-----------+----------+----------------------------------
 id           | integer |           | not null | nextval('salt_id_seq'::regclass)
 stormnumber  | integer |           |          |
 date         | date    |           |          |
 manhattan    | integer |           |          |
 bronx        | integer |           |          |
 brooklyn     | integer |           |          |
 queens       | integer |           |          |
 statenisland | integer |           |          |
 totaltons    | integer |           |          |
 average      | integer |           |          |
Indexes:
    "salt_pkey" PRIMARY KEY, btree (id)


#03- setting the value of the new column (average)

UPDATE salt
SET average = (ROUND(manhattan + bronx + brooklyn + queens + statenisland)/5);


 id | stormnumber |    date    | manhattan | bronx | brooklyn | queens | statenisland | totaltons | average
----+-------------+------------+-----------+-------+----------+--------+--------------+-----------+---------
  1 |           1 | 2016-01-19 |      1111 |  2059 |     2690 |   6625 |         2931 |     15416 |    3083
  2 |           2 | 2016-01-23 |      2919 |  4567 |     5521 |   9253 |         4264 |     26524 |    5305
  3 |           2 | 2016-01-24 |      6582 |  8167 |    12290 |  17133 |         5411 |     49583 |    9917
  4 |           2 | 2016-01-25 |      3862 |  4094 |     6217 |  10236 |         1256 |     25665 |    5133
  5 |           2 | 2016-01-26 |      2499 |  3299 |     5120 |   7685 |          764 |     19367 |    3873
(5 rows)


#04- unique values for year in date column

SELECT DISTINCT EXTRACT(YEAR FROM date)
FROM salt;


 date_part
-----------
      2016
      2017
      2019
      2018
(4 rows)


#05- total amount of salt used per year (aggregate fn)

SELECT EXTRACT(YEAR FROM date) as year, SUM(totaltons) as year_total
FROM salt
GROUP BY EXTRACT(YEAR FROM date);


 year | year_total
------+------------
 2016 |     304019
 2017 |     418526
 2019 |     289354
 2018 |     419017
(4 rows)


#06- years in which the total amount of salt used exceeded 400,000 tons

SELECT EXTRACT(YEAR FROM date) as year, SUM(totaltons) as year_total
FROM salt
GROUP BY EXTRACT(YEAR FROM date)
HAVING SUM(totaltons) > 400000;


 year | year_total
------+------------
 2017 |     418526
 2018 |     419017
(2 rows)


#07- months/years in which over 100,000 tons of salt were used

SELECT EXTRACT(MONTH FROM date) as month, EXTRACT(YEAR FROM date) as year, SUM(totaltons) as year_total
FROM salt
GROUP BY EXTRACT(MONTH FROM date), EXTRACT(YEAR FROM date)
HAVING SUM(totaltons) > 100000
ORDER BY year, month;


 month | year | year_total
-------+------+------------
     1 | 2016 |     180259
     2 | 2017 |     108424
     3 | 2017 |     131780
     1 | 2018 |     186252
     3 | 2018 |     119917
     2 | 2019 |     116579
(6 rows)


#08- number of storms which required the use of salt in each year recorded

SELECT EXTRACT(YEAR FROM date) as year, COUNT(DISTINCT stormnumber) as number_of_storms
FROM salt
GROUP BY EXTRACT(YEAR FROM date);


 year | number_of_storms
------+------------------
 2016 |                5
 2017 |                7
 2018 |               12
 2019 |                7
(4 rows)


#09- top 5 storms for which the most salt was used

SELECT EXTRACT(YEAR FROM date) as year, stormnumber, SUM(totaltons) as salt_used
FROM salt
GROUP BY stormnumber, EXTRACT(YEAR FROM date)
ORDER BY SUM(totaltons) DESC
LIMIT 5;


 year | stormnumber | salt_used
------+-------------+-----------
 2016 |           2 |    192455
 2017 |           7 |    115524
 2018 |           4 |    112417
 2017 |           5 |     92266
 2017 |           2 |     75893
(5 rows)


#10- days on which the DSNY had to salt roads/sidewalks relating to storm number 2 from 2016, the storm for which the most salt was used

SELECT date, stormnumber, manhattan, bronx, brooklyn, queens, statenisland, totaltons
FROM salt
WHERE EXTRACT(YEAR FROM date) = 2016 AND stormnumber = 2;


    date    | stormnumber | manhattan | bronx | brooklyn | queens | statenisland | totaltons
------------+-------------+-----------+-------+----------+--------+--------------+-----------
 2016-01-23 |           2 |      2919 |  4567 |     5521 |   9253 |         4264 |     26524
 2016-01-24 |           2 |      6582 |  8167 |    12290 |  17133 |         5411 |     49583
 2016-01-25 |           2 |      3862 |  4094 |     6217 |  10236 |         1256 |     25665
 2016-01-26 |           2 |      2499 |  3299 |     5120 |   7685 |          764 |     19367
 2016-01-27 |           2 |      2609 |  2007 |     4619 |   5656 |         1830 |     16721
 2016-01-28 |           2 |      1878 |  2017 |     2889 |   4090 |          560 |     11434
 2016-01-29 |           2 |       906 |  1652 |     2647 |   2829 |          338 |      8372
 2016-01-30 |           2 |       569 |  1134 |     1101 |   1675 |           75 |      4554
 2016-01-31 |           2 |       379 |   598 |      426 |   1140 |           80 |      2623
 2016-02-01 |           2 |       202 |   453 |      120 |    792 |            0 |      1567
 2016-02-02 |           2 |        66 |   302 |      276 |    448 |            0 |      1092
 2016-02-03 |           2 |        34 |   288 |      144 |    452 |            0 |       918
 2016-02-04 |           2 |         0 |    73 |        0 |    277 |            0 |       350
 2016-02-05 |           2 |      1495 |  1631 |     4641 |   7885 |         2054 |     17706
 2016-02-06 |           2 |       127 |   596 |     1822 |   2597 |          440 |      5582
 2016-02-08 |           2 |        26 |    28 |        0 |    303 |           40 |       397
(16 rows)
