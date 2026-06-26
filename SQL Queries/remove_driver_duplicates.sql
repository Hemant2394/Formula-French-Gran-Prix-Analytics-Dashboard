
select driverId, count(*) from driver_data group by driverId having count(*)>1;
select * from driver_data where driverId in (830,844);
create table driver_data_temp
select distinct * from driver_data;
truncate table driver_data;
insert into driver_data select * from driver_data_temp;
drop table driver_data_temp;