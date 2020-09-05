-- rank the country of origin of bands,
-- ordered by the number of (non-unique) fans
-- Column names must be: origin and nb_fans
SELECT origin, count(fans) AS "nb_fans"
FROM metal_bands
GROUP BY origin
ORDER BY count(fans) DESC
