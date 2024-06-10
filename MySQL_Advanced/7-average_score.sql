-- Finds average score per user
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id FLOAT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Calculate the average score for the given user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update the user's average score
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END//

DELIMITER ;