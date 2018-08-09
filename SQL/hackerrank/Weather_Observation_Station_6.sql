-- https://www.hackerrank.com/challenges/weather-observation-station-6/problem

# 1st solution
SELECT CITY
FROM STATION
WHERE CITY LIKE 'a%' or CITY LIKE 'e%' or CITY LIKE 'i%' or CITY LIKE 'o%' or CITY LIKE 'u%';


# 2nd solution
SELECT DISTINCT city 
FROM station
WHERE city REGEXP "^[aeiou].*";