-- Create a table, users
-- id, email, name
CREATE TABLE IF NOT EXISTS users (
       id INT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       CNSTRAINT users_pk PRIMARY KEY (id)
       )
