create table address (id serial primary key, staff_no int,address varchar(100), foreign key (staff_no) references staff (staff_no));
