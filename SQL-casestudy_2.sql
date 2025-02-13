/*Creating a database name LibraryDB*/
create database LibraryDB;

use LibraryDB;

/*Creating Books table*/
create table Books(
id int primary key auto_increment,
title varchar(100) not null,
author varchar(50) not null,
published_year year not null,
genre varchar(30)
);

/*Inserting values into books table*/
insert into Books values
(1,'Harry Potter','Rowling',1977,'Fantasy'),
(2,'jungle book','Smith',1989,'Adventure'),
(3,'Cindrella','Emiy',2005,'Children fiction'),
(4,'The horror land','Arin',1955,'Horror'),
(5,'The kittens tale','Hannah',2007,'Comedy');

/*Creating members table*/
create table members(
id int primary key auto_increment,
name varchar(50) not null,
membership_date date not null
);

/*Inserting values to members table*/
insert into members values
(1009,'Kousi','2025-01-05'),
(1007,'Regana','2024-09-05'),
(1004,'Nags','2024-03-22'),
(1002,'Nivi','2023-06-30'),
(1010,'Karthika','2025-01-20'),
(1003,'Hema','2023-10-17'),
(1008,'Koushika','2024-09-20'),
(1001,'Basheera','2023-03-01'),
(1005,'Hiba','2024-04-23'),
(1006,'Haritha','2024-06-28')
;

/*Creating borrowing  table*/
create table borrowing(
id int primary key auto_increment,
book_id int,
member_id int,
borrow_date date not null,
return_date date,
foreign key (member_id) references members(id)
);


/*Inserting values to borrowing table*/
insert into borrowing(book_id,member_id,borrow_date,return_date) values
(3,1007,'2024-10-20','2024-12-10'),
(4,1001,'2023-08-08','2023-11-30'),
(1,1002,'2024-01-05','2024-02-28'),
(2,1009,'2025-01-03','2025-01-25'),
(5,1010,'2025-01-20','2025-01-26'),
(3,1005,'2024-07-15','2024-08-11')
;
insert into borrowing(book_id,member_id,borrow_date,return_date) values
(4,1007,'2024-10-20','2024-12-10');

/*List all books*/
select title from Books;

/*List all members*/
select id,name from members;

/*Show borrowing records with member names and book titles*/
select members.name as members, Books.title as Book_title
from borrowing
inner join members on borrowing.member_id=members.id
inner join books on borrowing.book_id=books.id;

/*Count the number of books borrowed by each member*/
select members.name as member, count(books.title) as book_count
from borrowing
inner join members on borrowing.member_id=members.id
inner join Books on borrowing.book_id=books.id
group by members.name;



