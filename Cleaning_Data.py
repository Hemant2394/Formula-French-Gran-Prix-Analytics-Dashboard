import pandas as pd
race=pd.read_csv("races.csv")
race=race.drop(columns=["time","url","fp1_date","fp1_time","fp2_date","fp2_time","fp3_date","fp3_time"
                        ,"quali_date","quali_time","sprint_date","sprint_time"])
race=race[(race["year"]==2021) & (race["name"]=="French Grand Prix")]

driver=pd.read_csv("drivers.csv")
driver=driver.drop(columns=["url","nationality","dob","number","code","driverRef"])

lap=pd.read_csv("lap_times.csv")
lap=lap.drop(columns="time")
lap["milliseconds"]=lap["milliseconds"]/1000
lap=lap.rename(columns={"milliseconds":"seconds"})

pit=pd.read_csv("pit_stops.csv")
pit=pit.drop(columns=["time","milliseconds"])
driver=driver.merge(pit,on="driverId")
driver=driver.drop(columns=["stop","lap","duration"])
merge_pit=race.merge(pit,on="raceId")
merge_lap=race.merge(lap,on="raceId")
merge_driver=race.merge(driver,on="raceId")


merge_pit.to_csv('pit_Clean.csv', index=False)
merge_lap.to_csv('lap_clean.csv',index=False)
merge_driver.to_csv('driver_clean.csv',index=False)