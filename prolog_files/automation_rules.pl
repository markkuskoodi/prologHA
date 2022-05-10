/*
rule :-
    % Kontrollime, kas telekas töötab
    actuator("switch.tv_switch", on),
	% Teeme kindlaks mis seadmed meil grupis on
	group_scope("group.living_room", Scope),
	% Otsime välja õige domeeniga seadmed grupist
	domain_scope("light", Scope, Final_Scope),
	% Kuna reegliks on valguse vähendamine ruumis, siis vähendame valgust
	light_sensor("sensor.motion_sensor_light_level", low, Final_Scope).

rule2 :-
    time_comparison("15:00:00", "23:59:59"),
    person_status(_, home),
    actuator("switch.tv_switch", off),
    domain_scope("light", Scope),
    group_scope("group.living_room", Scope, Final_Scope),
    light_sensor("sensor.motion_sensor_light_level", high, Final_Scope).

rule3 :-
    light_sensor_status("sensor.outside_light_density", low),
    sensor("switch.livingroom_window", off),
    actuator_action("light.living_room_light", on).
*/

automatsiooni_reegel :-
    light_sensor_status("sensor.outside_light_density", low),
    actuator_action("light.kitchen_light_1", on).

automatsiooni_reegel2 :-
    temperature_sensor_status("sensor.outside_temperature", low),
    actuator_action("climate.air_conditioner", heat, mode).