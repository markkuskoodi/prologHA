kitchen_light_on :-
    light_sensor("sensor.outside_light_density", low),
    light_switch("switch.kitchen_light", off),
    retract(light_switch("switch.kitchen_light", off)),
	assertz(light_switch("switch.kitchen_light", on)).


living_room_light_on :-
    light_sensor("sensor.outside_light_density", low),
    light_switch("switch.living_room_light", off),
    retract(light_switch("switch.living_room_light", off)),
    assertz(light_switch("switch.living_room_light", on)).

