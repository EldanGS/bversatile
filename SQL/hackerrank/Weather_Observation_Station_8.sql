-- https://www.hackerrank.com/challenges/weather-observation-station-8/problem

SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[aeiou].*[aeiou]$';

/*


^			// start of string
[aeiou]		// a single vowel
.			// any characted...
*			// ...repeated any number of times
[aeiou]		// another vowel
$			// end of string


*/