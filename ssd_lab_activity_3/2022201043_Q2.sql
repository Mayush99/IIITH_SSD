Select concat(temp.Fname,' ',temp.Minit,' ',temp.Lname) as Full_name, Dname, Dnumber, Mgr_ssn, temp.no_of_employees from DEPARTMENT JOIN (SELECT sup.Ssn, sup.Fname, sup.Minit, sup.Lname, count(sub.Ssn) AS no_of_employees FROM EMPLOYEE sub JOIN EMPLOYEE sup ON sub.Super_ssn = sup.Ssn GROUP BY sup.Ssn, sup.Fname,
sup.Lname) as temp ON Mgr_ssn=temp.Ssn;

