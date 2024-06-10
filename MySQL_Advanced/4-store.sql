DELIMITER //

CREATE TRIGGER trigger
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.order_quantity
	WHERE item_id = NEW.item_id
END//

DELIMITER ;
