alter table driver_data
add constraint pk_driver_data primary key (driverId);
alter table lap_data
add constraint fk_lap_data foreign key (driverId) references driver_data(driverId);
alter table pit_data
add constraint fk_pit_data foreign key (driverId) references driver_data(driverId);
