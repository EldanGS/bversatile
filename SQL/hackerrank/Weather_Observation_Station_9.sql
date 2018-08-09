-- https://www.hackerrank.com/challenges/weather-observation-station-9/problem

# 1st solution.
SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTR(CITY, 1, 1) NOT IN ('a','i','o','e','u');


# 2nd solution.
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[^aeiou]';

