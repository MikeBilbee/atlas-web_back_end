-- Does a thing (delimits)
DELIMITER //

CREATE TRIGGER trigger
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.order_quantity
	WHERE name = NEW.item_id
END//

DELIMITER ;
