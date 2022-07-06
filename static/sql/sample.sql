insert into user_old(
	user_old_id,
	user_old_name,
	user_old_age,
	user_old_IDcard,
	user_old_address,
	user_old_number,
	user_old_logname,
	user_old_logpasswd,
	user_old_health_document_id
)
values (
	1,
	"user_old_1",
	60,
	"11111111111111111",
	"101 at Street A",
	"111111",
	"User_old_name1",
	"User_old_passwd1",
	1
);

insert into user_old(
	user_old_id,
	user_old_name,
	user_old_age,
	user_old_IDcard,
	user_old_address,
	user_old_number,
	user_old_logname,
	user_old_logpasswd,
	user_old_health_document_id
)
values (
	2,
	"user_old_2",
	48,
	"22222222222222222",
	"102 at Street A",
	"222222",
	"User_old_name2",
	"User_old_passwd2",
	2
);

insert into user_old(
	user_old_id,
	user_old_name,
	user_old_age,
	user_old_IDcard,
	user_old_address,
	user_old_number,
	user_old_logname,
	user_old_logpasswd,
	user_old_health_document_id
)
values (
	3,
	"user_old_3",
	65,
	"33333333333333333",
	"103 at Street B",
	"333333",
	"User_old_name3",
	"User_old_passwd3",
	3
);


insert into user_old(
	user_old_id,
	user_old_name,
	user_old_age,
	user_old_IDcard,
	user_old_address,
	user_old_number,
	user_old_logname,
	user_old_logpasswd,
	user_old_health_document_id
)
values (
	4,
	"user_old_4",
	80,
	"44444444444444444",
	"104 at Street B",
	"444444",
	"User_old_name4",
	"User_old_passwd4",
	4
);



insert into user_relative(
	user_relative_id,
	user_relative_name,
	user_relative_IDcard,
	user_relative_logname,
	user_relative_logpasswd
)
values(
	1,
	"user_relative1",
	"XXX",
	"user_relative_name1",
	"user_relative_passwd1"
);


insert into user_relative(
	user_relative_id,
	user_relative_name,
	user_relative_IDcard,
	user_relative_logname,
	user_relative_logpasswd
)
values(
	2,
	"user_relative2",
	"XXX",
	"user_relative_name2",
	"user_relative_passwd2"
);

insert into user_relative(
	user_relative_id,
	user_relative_name,
	user_relative_IDcard,
	user_relative_logname,
	user_relative_logpasswd
)
values(
	3,
	"user_relative3",
	"XXX",
	"user_relative_name3",
	"user_relative_passwd3"
);


insert into user_relative(
	user_relative_id,
	user_relative_name,
	user_relative_IDcard,
	user_relative_logname,
	user_relative_logpasswd
)
values(
	4,
	"user_relative4",
	"XXX",
	"user_relative_name4",
	"user_relative_passwd4"
);


insert into user_relative(
	user_relative_id,
	user_relative_name,
	user_relative_IDcard,
	user_relative_logname,
	user_relative_logpasswd
)
values(
	5,
	"user_relative5",
	"XXX",
	"user_relative_name5",
	"user_relative_passwd5"
);

insert into user_neighbor(
	user_neighbor_id,
	user_neighbor_name,
	user_neighbor_address,
	user_neighbor_number,
	user_neighbor_risk,
	user_neighbor_logname,
	user_neighbor_logpasswd
)
values(
	1,
	"user_neighbor1",
	"Stree A",
	"1111",
	"low",
	"user_neighbor_name1",
	"user_neighbor_passwd1"
);

insert into user_neighbor(
	user_neighbor_id,
	user_neighbor_name,
	user_neighbor_address,
	user_neighbor_number,
	user_neighbor_risk,
	user_neighbor_logname,
	user_neighbor_logpasswd
)
values(
	2,
	"user_neighbor2",
	"Stree B",
	"2222",
	"low",
	"user_neighbor_name2",
	"user_neighbor_passwd2"	
);

insert into rel_old_relative(
	rel_old_relative_old_id,
	rel_old_relative_relative_id
)
values (
	1,
	1
);



insert into rel_old_relative(
        rel_old_relative_old_id,
        rel_old_relative_relative_id
)
values (
        2,
        2
);

insert into rel_old_relative(
        rel_old_relative_old_id,
        rel_old_relative_relative_id
)
values (
        3,
        3
);

insert into rel_old_relative(
        rel_old_relative_old_id,
        rel_old_relative_relative_id
)
values (
        4,
        4
);

insert into rel_old_neighbor(
	rel_old_neighbor_old_id,
	rel_old_neighbor_neighbor_id
)
values(
	1,
	1
);

insert into rel_old_neighbor(
        rel_old_neighbor_old_id,
        rel_old_neighbor_neighbor_id
)
values(
        2,
        1
);

insert into rel_old_neighbor(
        rel_old_neighbor_old_id,
        rel_old_neighbor_neighbor_id
)
values(
        3,
        2
);

insert into rel_old_neighbor(
        rel_old_neighbor_old_id,
        rel_old_neighbor_neighbor_id
)
values(
        4,
        2
);

insert into sys_call(
	sys_call_id,
	sys_call_time,
	sys_call_type,
	sys_call_status,
	sys_call_old_id
)
values(
	1,
	'2022-07-05 10:00:00',
	1,
	"done",
	1
);

insert into sys_call(
	sys_call_id,
	sys_call_time,
	sys_call_type,
	sys_call_status,
	sys_call_old_id
)
values(
	2,
	'2022-07-06 08:00:00',
	2,
	"done",
	2
);

insert into sys_call(
	sys_call_id,
	sys_call_time,
	sys_call_type,
	sys_call_status,
	sys_call_old_id
)
values(
	3,
	'2022-07-06 22:00:00',
	2,
	"waiting",
	3
);

insert into sys_call(
	sys_call_id,
	sys_call_time,
	sys_call_type,
	sys_call_status,
	sys_call_old_id
)
values(
	4,
	'2022-07-04 12:00:00',
	1,
	"done",
	4
);
