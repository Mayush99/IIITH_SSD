CREATE PROCEDURE `SelectNameGrade` ()
BEGIN
SELECT CUST_NAME,GRADE FROM customer WHERE OPENING_AMT+RECEIVE_AMT>10000;
END
