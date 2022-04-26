allRules :- [init_preds, automation_rules].
light_status("light.kitchen_light_group", off).
climate_mode_status("climate.air_conditioner", off).
climate_temperature_status("climate.air_conditioner", 21).
climate_fan_status("climate.air_conditioner", low).
climate_swing_status("climate.air_conditioner", off).
climate_mode_status("climate.water_boiler", off).
climate_temperature_status("climate.water_boiler", 55).
light_status("light.kitchen_light_1", off).
light_status("light.kitchen_light_2", off).
light_status("light.living_room_light", off).
switch_status("switch.kitchen_window", off).
switch_status("switch.livingroom_window", off).
temperature_sensor("sensor.outside_temperature", medium).
temperature_sensor("sensor.kitchen_temperature", medium).
temperature_sensor("sensor.living_room_temperature", medium).
light_sensor("sensor.outside_light_density", low).

write_output(Response):-
	open('automation_results/2022_04_26_00_05_26.txt', append, Out),
	write(Out, Response),
	close(Out).

