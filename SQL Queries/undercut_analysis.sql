use project_1;
select driverId,avg(duration) as avg_duration from pit_data group by driverId order by avg_duration asc;
select driverId,min(seconds) from lap_data group by driverId;
select driverId,lap,seconds from lap_data order by seconds asc limit 20;