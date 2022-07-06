drop database zhkyDB;
create database if not exists zhkyDB;
use zhkyDB;


create table  if not exists user_old(
	user_old_id int  primary key,
	user_old_name varchar(100) not null,
	user_old_age int,
	user_old_IDcard varchar(20) not null,
	user_old_address varchar(100),
	user_old_number varchar(20),
	user_old_logname varchar(100) not null,
	user_old_logpasswd varchar(100) not null,
	user_old_health_document_id int not null
	)engine=InnoDB default charset=utf8;
	
create table  if not exists user_relative(
	user_relative_id int  primary key,
	user_relative_name varchar(100) not null,
	user_relative_age int,
	user_relative_IDcard varchar(20) not null,
	user_relative_address varchar(100),
	user_relative_number varchar(20),
	user_relative_logname varchar(100) not null,
	user_relative_logpasswd varchar(100) not null
	)engine=InnoDB default charset=utf8;
	

create table if not exists user_neighbor(
	user_neighbor_id int primary key,
	user_neighbor_name varchar(20) not null,
	user_neighbor_address varchar(100) not null,
	user_neighbor_number varchar(20) not null,
	user_neighbor_risk varchar(20) not null,
	user_neighbor_logname varchar(100) not null,
	user_neighbor_logpasswd varchar(100) not null
);



create table if not exists rel_old_relative(
	rel_old_relative_old_id int,
	rel_old_relative_relative_id int,
	primary key(rel_old_relative_old_id,rel_old_relative_relative_id),
	foreign key(rel_old_relative_old_id) references user_old(user_old_id),
	foreign key(rel_old_relative_relative_id) references user_relative(user_relative_id),
	constraint cons1 foreign key(rel_old_relative_old_id) references user_old(user_old_id) on DELETE cascade,
	constraint cons2 foreign key(rel_old_relative_relative_id) references user_relative(user_relative_id) on DELETE cascade
);

create table if not exists rel_old_neighbor(
	rel_old_neighbor_old_id int,
	rel_old_neighbor_neighbor_id int,
	primary key(rel_old_neighbor_old_id,rel_old_neighbor_neighbor_id),
	foreign key(rel_old_neighbor_old_id) references user_old(user_old_id),
	foreign key(rel_old_neighbor_neighbor_id) references user_neighbor(user_neighbor_id),
	constraint cons3 foreign key(rel_old_neighbor_old_id) references user_old(user_old_id) on DELETE cascade,
	constraint cons4 foreign key(rel_old_neighbor_neighbor_id) references user_neighbor(user_neighbor_id) on DELETE cascade
);

create table if not exists sys_call(
	sys_call_id int primary key, 
	sys_call_time varchar(30) not null,
	sys_call_type int not null,
	sys_call_status varchar(20) not null,
	sys_call_old_id int,
	constraint cons5 foreign key(sys_call_old_id) references user_old(user_old_id) on DELETE cascade
);
