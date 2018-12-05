DELIMITER $$
CREATE DEFINER=`root`@`192.168.20.113` PROCEDURE `sp_createUser`(
	IN p_id VARCHARACTER(45),
    IN p_name VARCHARACTER(45),
  	IN p_idname VARCHARACTER(45),
    IN p_password VARCHARACTER(45)
)
BEGIN
    if ( select exists (select 1 from `member` where id_name = p_idname) ) THEN
     
        select 'Username Exists !!';
     
    ELSEIF ( select exists (select 1 from `member` where id = p_id) ) THEN
    
    	select 'Id Exists !!';
    
    ELSE
     
        insert into `member`
        (
        	id,
            id_name,
            name,
            password
        )
        values
        (
        	p_id,
            p_name,
            p_idname,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;