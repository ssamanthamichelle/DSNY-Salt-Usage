--Samantha Michelle Garcia

--01 Total number of rows in the table

SELECT COUNT(*)
FROM salt;


--02 adding a new column without a default value

ALTER TABLE salt
ADD COLUMN average int;


--03 setting the value of the new column (average)

UPDATE salt
SET average = (ROUND(manhattan + bronx + brooklyn + queens + statenisland)/5);


--04 unique values for year in date column

SELECT DISTINCT EXTRACT(YEAR FROM date)
FROM salt;


--05 total amount of salt used per year (aggregate function)

SELECT EXTRACT(YEAR FROM date) as year, SUM(totaltons) as year_total
FROM salt
GROUP BY EXTRACT(YEAR FROM date);


--06 years in which the total amount of salt used exceeded 400,000 tons

SELECT EXTRACT(YEAR FROM date) as year, SUM(totaltons) as year_total
FROM salt
GROUP BY EXTRACT(YEAR FROM date)
HAVING SUM(totaltons) > 400000;


--07 months/years in which over 100,000 tons of salt were used

SELECT EXTRACT(MONTH FROM date) as month, EXTRACT(YEAR FROM date) as year, SUM(totaltons) as year_total
FROM salt
GROUP BY EXTRACT(MONTH FROM date), EXTRACT(YEAR FROM date)
HAVING SUM(totaltons) > 100000
ORDER BY year, month;


--08 number of storms which required the use of salt in each year recorded

SELECT EXTRACT(YEAR FROM date) as year, COUNT(DISTINCT stormnumber) as number_of_storms
FROM salt
GROUP BY EXTRACT(YEAR FROM date);


--09 top 5 storms for which the most salt was used

SELECT EXTRACT(YEAR FROM date) as year, stormnumber, SUM(totaltons) as salt_used
FROM salt
GROUP BY stormnumber, EXTRACT(YEAR FROM date)
ORDER BY SUM(totaltons) DESC
LIMIT 5;


--10 days on which the DSNY had to salt roads/sidewalks relating to storm number 2 from 2016, the storm for which the most salt was used

SELECT date, stormnumber, manhattan, bronx, brooklyn, queens, statenisland, totaltons
FROM salt
WHERE EXTRACT(YEAR FROM date) = 2016 AND stormnumber = 2;
