select concat(e.Fname,' ',e.Minit,' ',e.Lname) as Full_name, d.Mgr_ssn as ssn, d.Dnumber as DeptId, d.Dname as Dept_name from DEPARTMENT d, EMPLOYEE e, WORKS_ON w where d.Dnumber=e.Dno AND d.Mgr_ssn=e.Ssn AND e.Ssn=w.Essn AND w.Hours<40 group by DeptId;

