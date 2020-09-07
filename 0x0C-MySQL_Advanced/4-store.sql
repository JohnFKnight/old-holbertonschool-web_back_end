-- Set trigger on items to reduce quantity
-- after insert into orders
DELIMITER $$
CREATE TRIGGER decrease_qty
       AFTER INSERT ON orders
       FOR EACH ROW
       BEGIN
		UPDATE items
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
	END; $$

DELIMITER ;
