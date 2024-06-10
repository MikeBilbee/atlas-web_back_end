-- Finds average score per user
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id FLOAT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Calculate the average score for the given user
    SET avg_score = (SELECT AVG(score) FROM corrections as c WHERE c.user_id = user_id);

    -- Update the user's average score
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END//

DELIMITER ;