-- creates a stored procedure AddBonus
-- that adds a new correction for a student.

DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
	INSERT INTO projects (name)
	SELECT project_name
	FROM projects
	WHERE NOT EXISTS (SELECT id from projects WHERE name = project_name) LIMIT 1;
		INSERT INTO corrections (user_id, id, score)
	       VALUES (user_id, @project_n, score);
END$$

DELIMITER ;
