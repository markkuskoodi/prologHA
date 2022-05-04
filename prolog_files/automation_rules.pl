rule :-
    actuator("switch.tv_switch", on),
	% Teeme kindlaks mis seadmed meil grupis on
	group_scope("group.living_room", Scope),
	% Otsime välja õige domeeniga seadmed grupist
	domain_scope("light", Scope, Final_Scope),
	% Kuna reegliks on valguse vähendamine ruumis, siis vähendame valgust (either lülitame tule välja või laseme kaardina alla)
	light_sensor("sensor.motion_sensor_light_level", low, Final_Scope).

rule2 :-
    time_comparison("15:00:00", "23:59:59"),
    person_status(_, home),
    actuator("switch.tv_switch", off),
    domain_scope("light", Scope),
    group_scope("group.living_room", Scope, Final_Scope),
    light_sensor("sensor.motion_sensor_light_level", high, Final_Scope).

rule3 :-
    light_sensor_status("sensor.window_sensor_light_level", low),
    sensor("switch.window_switch", off),
    actuator_action("switch.test_light_1", "increase_light").

