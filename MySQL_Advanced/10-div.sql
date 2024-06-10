-- Divides 2 numbers and returns the result or 0
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    DECLARE result INT;

	--checks if second number is 0
    IF b = 0 THEN
        SET result = 0;

	--does division
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END //

DELIMITER ;
