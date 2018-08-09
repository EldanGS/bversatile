-- https://www.hackerrank.com/challenges/weather-observation-station-7/problem

SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTR(CITY, LENGTH(CITY), 1) IN ('a','i','o','e','u');