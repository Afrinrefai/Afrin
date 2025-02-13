/*Creating a new database*/
create database RetailDB;
use RetailDB;

/*Creating products table*/
create table products(
id int primary key auto_increment,
name varchar(50) not null,
price decimal(10,2) not null check(price>0),
stock int not null check(stock>=0)
);

/*Inserting data into products table*/
insert into products values
(101,'Shampoo',299.50,23),
(102,'Conditioner',467.80,7),
(103,'Serum',330.00,9),
(104,'Spray',440.57,30);

/*Creating suppliers table*/
create table suppliers(
id int primary key auto_increment,
name varchar(50) not null,
contact varchar(50)
);

/*Inserting data into suppliers table*/
insert into suppliers(name,contact) values
('Mama earth','mamaearth@gmail.com'),
('Minimalist','minimalist@gmail.com');

/*Creating sales table*/
create table sales(
id int primary key auto_increment,
product_id int,
date date not null,
quantity int not null check(quantity>0),
total_price decimal(10,2) not null,
foreign key (product_id) references products(id)
);

/*Inserting data into sales table*/
insert into sales(product_id,date,quantity,total_price) values
(101,'2025-01-06',3,898.50),
(104,'2025-01-07',1,440.57),
(103,'2025-01-08',4,1320.00),
(103,'2025-01-09',2,660.00),
(102,'2025-01-10',1,467.80),
(101,'2025-01-11',2,599.00),
(103,'2025-01-12',1,330),
(104,'2025-01-13',4,1762.28),
(102,'2025-01-14',2,935.60),
(101,'2025-01-15',5,1497.50);

/*Listing all products*/
select*from products;

/*Show products with stock less than 10*/
select name from products where stock<10;

/*List sales with product names and total prices*/
select products.name as product_names, sum(sales.quantity) as Total_sale_quantity
from sales
inner join products on sales.product_id=products.id
group by products.name;

/*Calculate the total sales for each product*/
select products.name, sum(sales.total_price) as Total_sales
from sales 
inner join products on sales.product_id=products.id
group by products.name;