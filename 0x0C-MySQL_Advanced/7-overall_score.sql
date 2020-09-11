-- creates a stored procedure ComputeOverallScoreForUser
-- that stores avg score of a student.

DELIMITER $$

CREATE PROCEDURE ComputeOverallScoreForUser(IN user_id INT)
BEGIN
	UPDATE users, corrections
	SET users.overall_score = 
	(SUM(corrections.score) / COUNT(corrections.id))
	WHERE corrections.user_id = user_id;
END$$

DELIMITER ;
