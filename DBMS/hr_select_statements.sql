/*  
Here we will learn to use the SELECT statement. And before we do, here are some facts about SELECT statement.
1. SQL stands for Structured Query Language.
2. We use this language to manage data in a database.
3. This allows to manage the data using tables. And we write queries using this language to fetch the data.
4. All the DBs (MsSQL, MySQL, Oracle, DB2, PostgreSQL, etc) support this language. 
5. It means that a query written on one DB will also work on other DB(s). Barring some extensions that are specific to DB(s)
6. This has been made possible as ISO made SQL a database standard.
*/

/*
For this exercise, we have created a database in the name hr. We will be quering various tables of this database to explain the features of SELECT statement.

Let's start exploring the features of a SELECT statement.
*/

/*
The belose USE statement makes the DB and active one. Which means, any reference to a table name will be checked for in this DB. 
If this statement is not used then you have to mention the DB name along with the table name using the notation DB.table_name
*/
USE hr;

/*
The easiest one. This lists all the rows and all the columns of each row of employee tables
 */
SELECT * FROM employees; 

/*
 If you wish to show only a few fields (columns) then you have to name each field explicitly in the SELECT statement
 If you mention all the column names explicitly then it will be equivalant to SELECT * statement
 */
SELECT first_name, last_name, phone_number FROM employees; 

/*
Using AS Clause: When you mention a column name with SELECT statement, you happen to see the column name. In order to make a column name more readable you 
can define a alias for a column name using AS clause. 
Notice that the column heading of first and last name has changed to the alias we have defined.
 */
SELECT first_name AS 'First Name', last_name AS 'Last Name', phone_number FROM employees; 

/*
Using DISTINCT Clause: When you want to view all the disctinct values of a particular column, you use a DISTINCT clause. 
 */
SELECT DISTINCT(job_id) FROM employees;

/*
Using DISTINCT Clause: In the below example we will get distinct values as combination of both job_id and first_name. 
 */
SELECT DISTINCT(job_id), first_name FROM employees;

/*
Summary functions - 
Using COUNT(*): When you want to know the number of rows in a table. 
 */
SELECT COUNT(*) FROM employees;

/*
Summary functions - 
Using SUM(field_name): give sum total of a field 
Using AVG(field_name): gives average of a field
Using MIN(field_name): gives minmum value of a field
Using MAX(field_name): gives maximum value of a field
 */
SELECT SUM(salary) as 'Total Monthly Salary', AVG(salary) as 'Average Salary', MIN(salary) as 'Min Salary', MAX(salary) as 'Max Salary' FROM employees;
#### Check the output when you give a non mumeric column name to these functions.


/*
Let's bring some order
ORDER BY clause
Use this to order the resutl on a particualr field or set of fields either in ascending or descending order
NOTE: Use order by as a last clause in a SQL statement
 */
SELECT * FROM employees ORDER BY job_id;
SELECT * FROM employees ORDER BY job_id desc; # in descebding order

/*
Let's bring some order
ORDER BY clause
Order by job_id in descending order and names within the job_id in ascending order;
 */
SELECT * FROM employees ORDER BY job_id desc, first_name;


/*
Let's bring some order
ORDER BY clause
Order a table in a particular sequence based on the values of a field;
 */
 SELECT * FROM employees ORDER BY field(job_id, 'ST_CLERK', 'SA_REP', 'SH_CLERK', 'SA_MAN', 'ST_MAN', 'PU_CLERK', 'IT_PROG', 'FI_ACCOUNT') DESC; 
 #### Check the output when you omit a few of the field values from the list. And you already know a way of getting the disctinct values of a field.
 
 
 /*
Filtering data
So far we have been pulling all the data that is available in a table. In reality, this will hardly be the case. We will always be interested in a single or a small
set of rows to work with. For this we use WHERE clause with various operators, wildcards and functions.
Using Operators: =, !=, <, <=, > and >=
Generally we use these operartors with numeric data. At the same time we can use these to compare the text data as well. Let's see
 */
SELECT * FROM employees WHERE employee_id  = 101;
SELECT * FROM employees WHERE employee_id  <= 110;
SELECT * FROM employees WHERE employee_id  > 200;
SELECT * FROM employees WHERE first_name  > 'Sunil';
#### Try to figure out as how we got this result.

/*
Filtering data
Using wildcards: Generally we use wildcards with LIKE clause. And we can combine these wildcard characters in an expression.
% - indicates 0 or more characters. 
_ - indicates exactly one character. 
 */
SELECT * FROM employees WHERE first_name LIKE 'S%'; # show all the rows where first name starts with S.
SELECT * FROM employees WHERE first_name LIKE 'S____'; # show all the rows where first name starts with S and has exactly 4 characters after S.
SELECT * FROM employees WHERE first_name LIKE 'S_n%'; # all rows with first name starts with S, any 1 charater after S. Third character is 'n'. followed by any or no characters

/*
Filtering data
Combining multiple conditions with 
AND - evaluates to True when both the conditions are True
OR - evaluates to True when eaither one the condition is True
NOT - toggles the result of a condition.
 */
SELECT * FROM employees WHERE employee_id  > 101 AND employee_id < 110; #show all employees with IDs between 101 and 110, excluding the boundary value.
SELECT * FROM employees WHERE employee_id  = 101 or employee_id = 110; 
SELECT * FROM employees WHERE employee_id  = 101 or employee_id = 210; 
SELECT * FROM employees WHERE employee_id  = 101 or employee_id = 210; 
SELECT * FROM employees WHERE commission_pct IS NULL;
SELECT * FROM employees WHERE commission_pct IS NOT NULL;


/*
Filtering data
Combining multiple conditions and changing the sequence of evaluation using brackets ()
 */
SELECT * FROM employees WHERE (employee_id > 101 AND employee_id < 110) OR job_id = 'FI_ACCOUNT'; 
SELECT * FROM employees WHERE (employee_id > 101 AND employee_id < 110) OR (employee_id > 151 AND employee_id < 160); 
SELECT * FROM employees WHERE (job_id = 'ST_CLERK' OR job_id = 'SA_REP') AND year(hire_date) > 1998;
SELECT * FROM employees WHERE job_id = 'ST_CLERK' OR job_id = 'SA_REP' AND year(hire_date) > 1998;
#### Analyse why the rows fetched in the above 2 satesments are different.

/*
Filtering data
Using IN and BETWEEN
Usage of IN and BETWEEN makes a query readable. Let's see it usage.
 */
SELECT * FROM employees WHERE employee_id = 101 OR employee_id = 102 OR employee_id = 103;
SELECT * FROM employees WHERE employee_id IN(101, 102, 103);
SELECT * FROM employees WHERE employee_id NOT IN(101, 102, 103);
SELECT * FROM employees WHERE job_id IN('ST_CLERK', 'SA_REP');

SELECT * FROM employees WHERE (employee_id >= 101 AND employee_id <= 110);
SELECT * FROM employees WHERE employee_id BETWEEN 101 AND 110;
SELECT * FROM employees WHERE employee_id NOT BETWEEN 101 AND 110;
SELECT * FROM employees WHERE first_name BETWEEN 'A%' AND 'C%';


/*
Limiting the output of rows
Using LIMIT clause

 */
SELECT * FROM employees; 
SELECT * FROM employees LIMIT 5; # shows first 5 records only
SELECT * FROM employees LIMIT 2, 5; # shows 5 records only starting afte 2nd row
 
 
/*
Grouping Data
We group data by using GROUP BY clause. 
Grouping is done to generate summary data rows based on the values of rows and expressions.
Each group returns 1 row that reduces the number of rows fetched.
This is used along with the the summary functions like SUM, AVG, MAX, MIN and COUNT
GROUP BY clause is written after the WHERE clause
 */
SELECT job_id, COUNT(*) as 'total' FROM employees GROUP BY job_id; 
SELECT job_id, COUNT(*) as 'total' FROM employees GROUP BY job_id ORDER BY total;
SELECT YEAR(hire_date) as 'Year', COUNT(*) as 'total' FROM employees GROUP BY year(hire_date);
SELECT department_id, Count(department_id), job_id, count(job_id) FROM employees GROUP BY department_id, job_id;
SELECT job_id, count(job_id) as 'Employee count', SUM(salary) as 'Total Monthly Salary', AVG(salary) as 'Average Salary', MIN(salary) as 'Min Salary', MAX(salary) as 'Max Salary' FROM employees GROUP BY job_id;

SELECT job_id, count(job_id) as 'Employee count', SUM(salary) as 'Total Monthly Salary', AVG(salary) as 'AverageSalary', MIN(salary) as 'Min Salary', MAX(salary) as 'Max Salary' 
FROM employees 
WHERE job_id in ('ST_CLERK', 'SA_REP', 'SH_CLERK')
GROUP BY job_id 
ORDER BY AverageSalary DESC;
# In order to use AverageSalary with ORDER BY clause, I have to remove space between thw two words.

/*
Filtering Grouped data
We can further filter the grouped data by using the HAVING clause
NOTE: we can also use HAVING clause without GROUP BY clause. In this case, the HAVING clause will work as WHERE clause
 */
SELECT job_id, count(job_id) as 'Employee count', SUM(salary) as 'Total Monthly Salary', AVG(salary) as 'AverageSalary', MIN(salary) as 'MinSalary', MAX(salary) as 'Max Salary' 
FROM employees 
WHERE job_id in ('ST_CLERK', 'SA_REP', 'SH_CLERK')
GROUP BY job_id 
HAVING MinSalary > 2200
ORDER BY AverageSalary DESC;
# In order to use AverageSalary with ORDER BY clause and MinSalary with HAVING clause, I have to remove space between thw two words.
SELECT * from employees HAVING job_id in ('ST_CLERK', 'SA_REP', 'SH_CLERK');
SELECT * from employees WHERE job_id in ('ST_CLERK', 'SA_REP', 'SH_CLERK');
 

/*
Joining tables
In RDBMS data is strored in various tables and these tables are related with each other using common keys (foreign keys) in tables.
In order to fetch information from these tables the data is fetched collectively and to do so joins are required.
A join a way of linking two tables using a value stored in the common columns of the tables
We will learn about 5 different type of joins

Inner join - It checks each row of first table against all the rows of the second table and returns a result when the common columns of both tables have same value

 */
SELECT first_name, last_name, job_title
FROM jobs, employees
Where employees.job_id = jobs.job_id;
/*
While working on the joins it is always a good practice to alias a table name. It is a good practice and very useful when you want to refer to a field name that is common to 
both the tables. In the below query, I have added job_id in the SELECT statement. Both the tables have this field. But MySQL does not know which table to refer to show 
the job_id. Hence an error in the execution of this query.
NOTE: when you mention 2 tables in a INNER join query, you can mention the table names in FROM clause in any sequence.
 */
SELECT job_id, first_name, last_name, job_title
FROM jobs, employees
Where employees.job_id = jobs.job_id; 

/*
Here is the suggested approach
 */
SELECT j.job_id, e.first_name, e.last_name, j.job_title
FROM jobs as j, employees as e
Where e.job_id = j.job_id; 
/*
Now I add 2 new entries in the jobs table. You will notice that these two jobs will not be listed when I run the above query. 
 */
INSERT INTO jobs (job_id, job_title, min_salary, max_salary) VALUES ( 'CX_CEO', 'Chief Executive Officer', 55000, 90000);
INSERT INTO jobs (job_id, job_title, min_salary, max_salary) VALUES ( 'CX_CTO', 'Chief Technical Officer', 55000, 90000);
SELECT j.job_id, e.first_name, e.last_name, j.job_title
FROM jobs as j, employees as e
Where e.job_id = j.job_id; 

/*
LEFT Join - In a left join, table on the left returns all the rows and the table on right returns rows when the common columns of both tables have same value. 
NULL value is returned for unmatching rows. 
Using the above example again, we apply left join. jobs table is on the LEFT side. So all of its rows will be returned. For the CX_ rows first_name and last_name 
will have null values.
*/
SELECT j.job_id, e.first_name, e.last_name, j.job_title
FROM jobs as j LEFT JOIN employees as e
ON e.job_id = j.job_id; 

/*
LEFT Join - In the below example the sequence of tables is changed. employees table is on the LEFT side.
*/
SELECT j.job_id, e.first_name, e.last_name, j.job_title
FROM employees as e LEFT JOIN jobs as j
ON e.job_id = j.job_id; 

/*
LEFT Join - Other styles are...
*/
SELECT j.job_id, e.first_name, e.last_name, j.job_title
FROM employees as e LEFT JOIN jobs as j
USING(job_id); 

SELECT j.job_id, e.first_name, e.last_name, j.job_title
FROM employees as e LEFT JOIN jobs as j
USING(job_id)
WHERE e.job_id = 'SH_CLERK'; # show the data only for SH_CLERK

/*
Right Join - In a right join, table on the right returns all the rows and the table on left returns rows when the common columns of both tables have same value. 
NULL is returned for unmatching rows
The syntax is same as of LEFT join. 
*/
SELECT j.job_id, e.first_name, e.last_name, j.job_title
FROM employees as e RIGHT JOIN jobs as j
USING(job_id); 


/*
Cross Join - his returns a cartesian product of the two tables. If table#1 has m rows and table#2 has n rows, then a cross join will return m*n rows
It is a SELECT statement with multiple tables with no WHERE clause. In case you mention a WHERE clause with the statement, it becomes an INNER join
*/
SELECT COUNT(*) FROM employees as e, jobs as j;

SELECT COUNT(*) from employees;
SELECT COUNT(*) from jobs;
SELECT 107*21 as 'Cross';


/*
SELF Join - A self join is done to either compare a row with another row  in the same table or to compare the hierarchal data in a table
When a self join is done, the table is aliased so as to provide a distinction to the two references of a table
*/
SELECT e1.employee_id, e1.first_name, e1.last_name, e2.employee_id, e2.first_name, e2.last_name 
FROM employees e1, employees e2
WHERE e1.employee_id = e2.manager_id
AND e1.employee_id = 100 ORDER BY e2.employee_id;


/* Sub Query / Inner Query
Sub query is a query which is nested in another query. In MySQL it is called inner query. It can be used along with the FROM and WHERE clause
*/

SELECT job_id FROM jobs WHERE job_id LIKE 'S%'; # we will use this as an inner query.
SELECT * from employees WHERE job_id in (SELECT job_id FROM jobs WHERE job_id LIKE 'S%');


SELECT d.department_name, SUM(salary) as 'sum_salary', Avg(salary) as 'avg_salary', Count(*) as 'Emp_Count'
FROM employees as e, departments as d
WHERE e.department_id = d.department_id 
GROUP BY e.department_id 
ORDER BY d.department_id; # We will use this along with FROM

SELECT * FROM(
SELECT d.department_name, SUM(e.salary) as 'sum_salary', Avg(e.salary) as 'avg_salary', Count(*) as 'Emp_Count'
FROM employees as e, departments as d
WHERE e.department_id = d.department_id 
GROUP BY e.department_id 
ORDER BY d.department_id) AS teml_table 
WHERE avg_salary > 5000;

# The below is same as above - slightly different implementation
SELECT d.department_name, SUM(e.salary) as 'sum_salary', Avg(e.salary) as 'avg_salary', Count(*) as 'Emp_Count'
FROM employees as e, departments as d
WHERE e.department_id = d.department_id 
GROUP BY e.department_id 
HAVING avg_salary > 5000
ORDER BY d.department_id;
