Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')

CREATE OR REPLACE FUNCTION NthHighestSalary(N INT)
RETURNS TABLE (Salary INT)
AS $$
BEGIN
    IF N<1 THEN 
        RETURN QUERY(SELECT NULL::INT salary);
    ELSE
        RETURN QUERY(
            SELECT DISTINCT e.salary
            FROM Employee e
            ORDER BY e.salary DESC
            LIMIT 1 OFFSET (N-1)
        );
    END IF;
END;
$$ LANGUAGE plpgsql;