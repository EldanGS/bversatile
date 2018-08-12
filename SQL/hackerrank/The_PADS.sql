-- https://www.hackerrank.com/challenges/the-pads/problem

SELECT CONCAT(Name, CONCAT('(', CONCAT(LEFT(Occupation,1),')')))  
FROM OCCUPATIONS
ORDER BY Name ASC;
                                       
SELECT CONCAT('There are a total of', CONCAT(' ', CONCAT(COUNT(Occupation), CONCAT(' ', CONCAT(LOWER(Occupation),'s.')))))
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(OCCUPATION), OCCUPATION ASC;
