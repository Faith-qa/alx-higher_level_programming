-- creates a table unique id
-- id INT default value 1 and must be unique name VANCHAR(254)
-- If table already exist script should not fail
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
