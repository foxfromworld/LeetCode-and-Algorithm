# Source : https://leetcode.com/problems/second-highest-salary/
# Author : foxfromworld
# Date  : 04/03/2021
# First attempt 

# I used this site to test:　https://paiza.io/projects/xiGLjFWheBbsJgJ1h0_ARg?language=mysql

create table If Not Exists Employee (Id int, Salary int);
TRUNCATE table Employee;
insert into Employee (Id, Salary) values ('1', '100');
insert into Employee (Id, Salary) values ('2', '200');
insert into Employee (Id, Salary) values ('3', '300');

SELECT( 
    SELECT DISTINCT Salary 
    FROM Employee 
    ORDER BY Salary DESC LIMIT 1,1 # return 1 row after skipping 1 row
) AS SecondHighestSalary
