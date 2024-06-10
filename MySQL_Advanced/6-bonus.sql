-- Creates a procedure for extra credit
DELIMITER//

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE project_id INT;

	-- Checks if project exists 
	IF NOT EXISTS (SELECT * FROM projects WHERE name = project_name) 
	THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;

	-- Creates and inserts correction
	SELECT id INTO project_id FROM projects WHERE name = project_name;
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END
//

DELIMITER ;
