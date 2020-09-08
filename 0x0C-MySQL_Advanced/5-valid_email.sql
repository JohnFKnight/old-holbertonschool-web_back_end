-- Set trigger on items to reduce quantity
-- after insert into orders
DELIMITER $$
CREATE TRIGGER set_valid_email
       BEFORE UPDATE ON users
       FOR EACH ROW
       BEGIN
		IF OLD.email <> NEW.email THEN
		   SET NEW.valid_email = 0;
		END IF;
	END; $$

DELIMITER ;
