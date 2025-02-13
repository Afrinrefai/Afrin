/*Creating database*/
create database StudentDB;
use StudentDB;

/*Creating table students*/
create table students(
id int primary key auto_increment,
name varchar(50) not null,
age int not null,
email varchar(50) not null unique);

/*Inserting value to student table*/
insert into students values
(101,'Afrin',22,'afrin@gmail.com'),
(102,'Ahmed Basheera',23,'bashh@gmail.com'),
(103,'Amara',21,'amara@gmail.com'),
(104,'Hiba',22,'hiba@gmail.com'),
(105,'Nags',21,'Nags@gmail.com')
;

/*Creating courses table */
create table courses(
id int primary key auto_increment,
name varchar(50) not null
);

/*Inserting value to Courses table*/
insert into courses(name) values
('Data Science'),
('AI'),
('Cloud computing')
;

/*Cretaing enrollments detail table*/
create table enrollments(
student_id int primary key,
course_id int ,
grade char(1),
foreign key (student_id) references students(id),
foreign key (course_id) references courses(id)
);

/*Inserting into enrollments table*/
insert into enrollments values
(101,2,'O'),
(102,3,'A'),
(103,1,'A'),
(104,2,'O'),
(105,1,'A')
;

/*List all students*/
select*from students;

/*List all courses*/
select*from courses;

/*Show the names of students and the courses they are enrolled in*/
select students.name as Student_name, courses.name as Course_enrolled
from enrollments
inner join students on enrollments.student_id=students.id
inner join courses on enrollments.course_id=courses.id;

/*Count the number of students in each course*/
select courses.name,count(students.name)
from enrollments
inner join students on enrollments.student_id=students.id
inner join courses on enrollments.course_id=courses.id
group by courses.name;