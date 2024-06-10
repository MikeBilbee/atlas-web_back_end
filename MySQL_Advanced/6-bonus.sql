-- Creates a procedure for extra credit
DELIMITER//

CREATE PRCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE project_id INT;

	-- Check for existing project
	SELECT id INTO project_id FROM projects WHERE name = project_name;

	-- Create project
	IF project_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET project_id = LAST_INSERT_ID();
	END IF;

	-- New Correction
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END
//

DELIMITER ;
