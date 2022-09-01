CREATE PROCEDURE `SelectAgent`()
BEGIN
    declare name VARCHAR(40);
    declare city VARCHAR(35);
    declare country VARCHAR(20);
    declare grade decimal(10,0);
    declare exit_loop integer default 0;
    declare cur cursor for select CUST_NAME, CUST_CITY, CUST_COUNTRY, GRADE from customer where AGENT_CODE like 'A00%';
    declare continue handler for NOT FOUND set exit_loop=1;
    open cur;
    CREATE TABLE agent_code(
    c_name varchar(40),
    c_city varchar(35),
    c_country varchar(20),
    c_grade decimal(10,0)
    );
    agent: LOOP
        fetch cur into name, city, country, grade;
        if exit_loop=1 then leave agent;
        end if;
        INSERT INTO agent_code VALUES(name,city,country,grade);
    END LOOP agent;
    SELECT * from agent_code;
    Drop table agent_code;
    close cur;
END
