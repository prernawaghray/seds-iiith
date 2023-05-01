show databases;
use hr;
show tables;
select * from employees;
select employee_id, first_name, last_name from employees;
select first_name, last_name, department_id, salary from employees where salary > 20000;
select first_name, last_name, email, salary, manager_id from employees where (manager_id = 120 or manager_id = 103 or manager_id = 145);
select first_name, last_name, department_id, salary from employees where ((manager_id = 120 or manager_id = 103 or manager_id = 145) and (salary > 8000));
select location_id, city from locations where state_province is null;
select * from jobs where max_salary > 10000;
select * from departments where (location_id = 1700 and manager_id is not null);
select * from departments where (department_name like 'P%' and manager_id is not null);
select '''This is to certify that ''', first_name, '''with employee id''', employee_id, '''is working as''', job_id, '''in dept''', department_id from employees where employee_id = 123;
select employee_id, salary,
case when salary >5000 then 'Tier1'
	when salary between 5000 and 10000 then 'Tier2' 
	when salary <10000 then 'Tier3'
end
from employees;
select job_id, department_id, salary from employees where salary > 2500 group by job_id, department_id, salary;
