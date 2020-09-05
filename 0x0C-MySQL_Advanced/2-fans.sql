-- rank the country of origin of bands,
-- ordered by the number of (non-unique) fans
-- Column names must be: origin and nb_fans
SELECT origin, COUNT(fans) AS "nb_fans"
FROM metal_bands
GROUP BY origin
HAVING COUNT(fans) > 1
ORDER BY COUNT(fans) DESC;
