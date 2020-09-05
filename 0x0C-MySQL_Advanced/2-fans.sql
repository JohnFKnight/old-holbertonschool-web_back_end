-- rank the country of origin of bands,
-- ordered by the number of (non-unique) fans
-- Column names must be: origin and nb_fans
SELECT origin, count(fans) AS "nb_fans"
FROM metal_bands
GROUP BY origin
ORDER BY count(fans) DESC

-- Create a table, users
-- Add country list
CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM('US', 'CO', 'TN'),
       PRIMARY KEY (id)
       )
