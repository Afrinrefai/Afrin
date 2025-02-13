/*Creating a database*/
create database LearningDB;
use LearningDB;

/*Creatinga a course table*/
create table courses(
id int primary key auto_increment,
title varchar(100) not null,
description text);

/*Inserting data into courses table*/
insert into courses(title,description) values
('Data science using python','Data Science: Extracting insights and patterns from data using statistical, analytical, and machine learning techniques.'),
('Business Analyst','Business Analysis (BA): Identifying business needs and recommending data-driven solutions to improve processes and strategies.'),
('Web development','Web Development: Building and maintaining websites and web applications using programming, design, and development frameworks.');

/*Creating a instructor table*/
create table instructors(
id int primary key auto_increment,
name varchar(50) not null,
expertise varchar(50) not null);

/*Inserting records into instructors table*/
insert into instructors(name,expertise) values 
('Joe Biden','Data Science'),
('Muhammad Ali','Business Intelligence'),
('Mike Tyson','Full stack developer');

/*Creating a student table*/
create table students(
id int primary key auto_increment,
name varchar(50) not null,
email varchar(50) not null unique);

/*Inserting values into students table*/
insert into students values
(101,'Afrin','afrin@gmail.com'),
(102,'Ahmed Basheera','bashh@gmail.com'),
(103,'Amara','amara@gmail.com'),
(104,'Hiba','hiba@gmail.com'),
(105,'Nags','Nags@gmail.com');

/*Creating enrollment detail table*/
create table enrollments(
student_id int,
course_id int,
enrollment_date date not null,
foreign key (student_id) references students(id),
foreign key (course_id) references courses(id));

/*Inserting values into enrollment table*/
insert into enrollments values
(101,2,'2024-09-22'),
(102,1,'2024-09-05'),
(103,3,'2024-09-30'),
(104,2,'2024-09-27'),
(104,1,'2024-09-18');

/*List all courses*/
select title from courses;

/*List all instructors*/
select name from instructors;

/*Show enrollments with student names and course titles*/
select students.name as Students, courses.title as Course_enrolled
from enrollments
inner join students on enrollments.student_id=students.id
inner join courses on enrollments.course_id=courses.id;

/*Count the number of students enrolled in each course*/
select courses.title as Students, count(students.name) as Course_enrolled
from enrollments
inner join students on enrollments.student_id=students.id
inner join courses on enrollments.course_id=courses.id
group by courses.title;