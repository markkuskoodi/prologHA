:-style_check(-discontiguous).
actuator("light.kitchen_light_group", off).
domain("light.kitchen_light_group", "light").
actuator_type("light.kitchen_light_group", light).
entity_type("light.kitchen_light_group", group).
climate_temperature_status("climate.air_conditioner", 21).
actuator("climate.air_conditioner", off, mode).
actuator("climate.air_conditioner", low, fan).
actuator("climate.air_conditioner", off, swing).
actuator_type("climate.air_conditioner", temperature).
domain("climate.air_conditioner", "temperature").
entity_type("climate.air_conditioner", single).
climate_temperature_status("climate.water_boiler", 55).
actuator("climate.water_boiler", off, mode).
actuator_type("climate.water_boiler", temperature).
domain("climate.water_boiler", "temperature").
entity_type("climate.water_boiler", single).
actuator("light.kitchen_light_1", off).
domain("light.kitchen_light_1", "light").
actuator_type("light.kitchen_light_1", light).
entity_type("light.kitchen_light_1", single).
actuator("light.kitchen_light_2", off).
domain("light.kitchen_light_2", "light").
actuator_type("light.kitchen_light_2", light).
entity_type("light.kitchen_light_2", single).
actuator("light.living_room_light", off).
domain("light.living_room_light", "light").
actuator_type("light.living_room_light", light).
entity_type("light.living_room_light", single).
actuator("switch.kitchen_window", off).
domain("switch.kitchen_window", "switch").
actuator_type("switch.kitchen_window", window).
entity_type("switch.kitchen_window", single).
actuator("switch.livingroom_window", on).
domain("switch.livingroom_window", "switch").
actuator_type("switch.livingroom_window", window).
entity_type("switch.livingroom_window", single).
temperature_sensor_status("sensor.outside_temperature", low).
domain("sensor.outside_temperature", "temperature").
entity_type("sensor.outside_temperature", single).
temperature_sensor_status("sensor.kitchen_temperature", medium).
domain("sensor.kitchen_temperature", "temperature").
entity_type("sensor.kitchen_temperature", single).
temperature_sensor_status("sensor.living_room_temperature", medium).
domain("sensor.living_room_temperature", "temperature").
entity_type("sensor.living_room_temperature", single).
light_sensor_status("sensor.outside_light_density", low).
domain("sensor.outside_light_density", "light").
entity_type("sensor.outside_light_density", single).

write_output(Response):-
	open('automation_results/2022_05_10_18_19_36.txt', append, Out),
	write(Out, Response),
	close(Out).

