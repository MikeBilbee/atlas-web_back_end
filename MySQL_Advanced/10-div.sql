-- Divides 2 numbers and returns the result or 0
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	--checks if second number is 0
    IF b = 0 THEN
	RETURN 0;
	--does division
    ELSE
        RETURN a / b;
    END IF;

END //

DELIMITER ;
