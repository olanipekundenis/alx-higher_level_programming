-- creates the table id_not_null on mysql database with 
-- name passed as an argument of mysql command
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1,
		name VARCHAR(256)
		);
