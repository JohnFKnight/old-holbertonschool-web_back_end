-- creates a stored procedure ComputeOverallScoreForUser
-- that stores avg score of a student.

DELIMITER $$

CREATE PROCEDURE ComputeOverallScoreForUser(IN user_id INT)
BEGIN
	UPDATE users
	SET overall_score = 
	SELECT (SUM(score) / count(*))
		FROM users
		WHERE id = user_id;
END$$

DELIMITER ;
