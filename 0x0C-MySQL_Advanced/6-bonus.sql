-- creates a stored procedure AddBonus
-- that adds a new correction for a student.

DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
	INSERT INTO projects (name)
	SELECT project_name
	FROM projects
	WHERE NOT EXISTS (SELECT id from projects WHERE name = project_name) LIMIT 1;
	SELECT id INTO @proj_id FROM projects WHERE name=project_name;
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, @proj_id, score);
END$$

DELIMITER ;
