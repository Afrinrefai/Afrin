/* Creating a database*/
Create database EmployeeManagement;

/*Use the created database*/
use EmployeeManagement;

/*Creating Department table*/
create table Departments(
id int primary key auto_increment,
name varchar(50) NOT NULL
);

DELETE FROM Departments
WHERE id IN (5,6,7,8,9,10,11,12);

/*Inserting values in Departments table*/
insert into Departments values(1,'Managing');
insert into Departments values(2,'HR');
insert into Departments values(3,'Production');
insert into Departments values(4,'Marketing');
insert into Departments values(5,'Sales');
/*Retrieving records from department table*/
select*from Departments;
update Departments 
set name='IT'
where id='3';

/*Retrieving records from department table*/
select*from Departments;

/*Creating Employee table*/
create table Employees(
id int primary key auto_increment,
name varchar(50) not null,
age int not null,
gender varchar(10) not null,
salary int not null check(salary>30000),
department_id int,
foreign key (department_id) references Departments(id)
);

/*Inserting records to Employee table*/
insert into Employees values(1001,'Williamson',38,'Male',150000,1);
insert into Employees values(1002,'Dhoni',35,'Male',120000,1);
insert into Employees values(2001,'Kholi',40,'Male',95000,2);
insert into Employees values(4001,'Moeen Ali',45,'Male',100000,4);
insert into Employees values(4002,'Head',28,'Male',50000,4);
insert into Employees values(5001,'Classen',48,'Male',60000,5);
insert into Employees values(2002,'Rabada',36,'Male',85000,2);
insert into Employees values(3001,'Chris Gayle',44,'Male',70000,3);
insert into Employees values(3002,'Cummins',39,'Male',80000,3);
insert into Employees values(4003,'Sachin',52,'Male',89000,4);
insert into Employees values(5002,'Ashwin',35,'Male',50000,5);
insert into Employees values(3003,'Gawaskar',60,'Male',75000,3);

/*Retrieving records from Employee table*/
select*from Employees;

select count(name) from Employees;

/*Creating Project table*/
create table Projects(
id int primary key auto_increment,
name varchar(50) not null,
budget int not null check(budget>10000)
);

/*Inserting values to Project table*/
insert into Projects values(51,'Alpha',400000);
insert into Projects values(52,'Beta',550000);
insert into Projects values(53,'Hiring',300000);

/*Retrieving records from projects table*/
select*from Projects;

/*Creating Employee_project table*/
create table Employee_projects(
employee_id int,
foreign key (employee_id) references Employees(id),
project_id int,
foreign key (project_id) references Projects(id)
);

/*Inserting values in Employee_projects table*/
insert into Employee_projects values(1001,51);
insert into Employee_projects values(1002,52);
insert into Employee_projects values(2001,53);
insert into Employee_projects values(2002,53);
insert into Employee_projects values(3001,51);
insert into Employee_projects values(3002,52);
insert into Employee_projects values(3003,52);
insert into Employee_projects values(4001,51);
insert into Employee_projects values(4002,51);
insert into Employee_projects values(4003,52);
insert into Employee_projects values(5001,51);
insert into Employee_projects values(5002,52);

/*Displaying records of Employee_projects table */
select*from Employee_projects;

/*Creating table for Attendance*/
create table Attendance(
id int primary key auto_increment,
employee_id int,
foreign key (employee_id) references Employees(id),
date date not null,
status enum('Present','Absent','On leave')
);

desc Attendance;

/*Inserting values into Attendance table*/
insert into Attendance values(1,1001,'2025-01-02','Present');
insert into Attendance values(2,1002,'2025-01-02','Present');
insert into Attendance values(3,2001,'2025-01-02','Present');
insert into Attendance values(4,2002,'2025-01-02','Present');
insert into Attendance values(5,3001,'2025-01-02','Absent');
insert into Attendance values(6,3002,'2025-01-02','Present');
insert into Attendance values(7,3003,'2025-01-02','Present');
insert into Attendance values(8,4001,'2025-01-02','On leave');
insert into Attendance values(9,4002,'2025-01-02','Present');
insert into Attendance values(10,4003,'2025-01-02','Present');
insert into Attendance values(11,5001,'2025-01-02','On leave');
insert into Attendance values(12,5002,'2025-01-02','Present');

/*Displaying records of Attendance table*/
select*from Attendance;

/* Retrieve all employees*/
select*from Employees;

/*Retrieve all empoyees in the IT department*/
select*from Employees where department_id=3;

/*List out projects with budget greater than 350000*/
select*from Projects where budget>350000;

/*Find employee with salary greater than 80000*/
select*from Employees where salary>80000;

/* Show names of employees and the projects they are working */
select Employees.name as Employee_Name, Projects.name as Project_Name
from Employees
inner join Employee_Projects on Employees.id = Employee_Projects.employee_id
inner join Projects on Employee_Projects.project_id = Projects.id;

/*Counts of employees in each department*/
select Departments.name as Department_Name, COUNT(Employees.id) as Employee_Count
from Employees
inner join Departments on Employees.department_id = Departments.id
group by Departments.name;

/*Find employees with a salary greater than 50000*/
select id,name,salary from Employees where salary>50000;

/*Get attendance records for a specific employee.*/
Select*from Attendance where employee_id=4001;

/*Increase the salary of employees in the 'HR' department by 10%*/
select Departments.name as Dept_name,sum(salary) as incremented_salary 
from Employees
inner join Departments on Employees.department_id = Departments.id
where Departments.name = 'HR';

Select*from Employees;
Select Departments.name as Department, Employees.salary as Salary
from Employees
inner join Departments on Employees.department_id = Departments.id;

update Employees
Inner join Departments on Employees.department_id=Departments.id
set Employees.salary=salary*1.10
where Departments.name='HR';

select*from Employees;

/*Change the department of an employee*/
update Departments 
set id=2003,name='HR'
where id=3003;

/*Add a unique constraint to the `email` column in `Employees` table*/
alter table Employees ADD 
email varchar(30) unique;

/*Ensure `age` is always greater than 18*/
alter table Employees modify
age int check (age>18);

/*Add a default value 'Unknown' to `gender` if not specified*/
alter table Employees modify
gender varchar(10) default 'unknown';











