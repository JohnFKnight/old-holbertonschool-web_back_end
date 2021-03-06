-- Create a table, users
-- Add country list
CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM('US', 'CO', 'TN'),
       PRIMARY KEY (id)
       )
