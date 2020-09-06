-- List bands by glam style
-- Ranked by their longevity
-- Column names must be: band_name and lifespan (in years)
-- You should use attributes formed and split for computing the lifespan
SELECT band_name,
       IFNULL(split, YEAR(CURRENT_DATE())) - formed AS "lifespan"
FROM metal_bands
WHERE   style LIKE '%Glam%'
GROUP BY band_name, lifespan
