create database employees;
create table staff(id serial primary key,staff_no int unique,fname varchar(100),lname varchar(100));
alter table staff add constraint staffno_uniq unique (staff_no);
