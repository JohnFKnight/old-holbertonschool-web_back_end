-- creates a stored procedure ComputeOverallScoreForUser
-- that stores avg score of a student.
   
DELIMITER $$

CREATE PROCEDURE ComputeOverallScoreForUser(IN user_id INT)
BEGIN
	UPDATE users
	SET users.overall_score = (SELECT
	SUM(score), COUNT(id), SUM(score)/COUNT(id)
	FROM collections
	WHERE user_id = user_id);
END$$

DELIMITER ;
