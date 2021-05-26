-- creates the table 'force_name'
-- id INT, VARCHAR(256) cant be NULL
-- If table exists script should not fail
CREATE TABLE IF NOT EXISTS force_name(id INT,
name VARCHAR(256) NOT NULL
);
