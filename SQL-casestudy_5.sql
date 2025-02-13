/*Creating a database*/
create database HospitalDB;
use HospitalDB;

/*Creating patients table*/
create table patients(
id int primary key auto_increment,
name varchar(50) not null,
age int not null,
gender varchar(10),
contact varchar(50));

insert into patients(id,name,age,gender,contact) values
(121,'Prem',37,'Male','prem@gmail.com'),
(122,'Ramya',45,'Female','Ramya123@gmail.com'),
(123,'Gita',20,'Female','gita@gmail.com'),
(124,'Krish',12,'Male','selvi@gmail.com'),
(125,'Vani',60,'Female','vanivani@gmail.com');

create table doctors(
id int primary key auto_increment,
name varchar(50) not null,
specialization varchar(50) not null);

insert into doctors(name,specialization) values
('Savitha','Ortho'),
('Ravi','Dermatologist');

create table appointments(
id int primary key auto_increment,
patient_id int,
doctor_id int,
appointment_date date not null,
status_ enum('Scheduled','Completed','Cancelled'));

insert into appointments(patient_id,doctor_id,appointment_date,status_) values
(121,1,'2025-01-04','Completed'),
(122,2,'2025-01-25','Cancelled'),
(123,1,'2025-01-26','Scheduled'),
(124,2,'2025-01-24','Completed'),
(125,2,'2025-01-26','Scheduled');

select*from patients;

select*from doctors;

select patients.name as Patient, doctors.name, appointments.appointment_date as Appointment_on
from appointments 
inner join patients on appointments.patient_id=patients.id
inner join doctors on appointments.doctor_id=doctors.id;

select doctors.name as Doctor, count(doctors.name)
from appointments
inner join doctors on appointments.doctor_id=doctors.id
group by doctors.name;

