:-dynamic( temperature_sensor/2 ).
temperature_sensor("sensor.outside_temperature", 10).
temperature_sensor("sensor.kitchen_temperature", 15).
temperature_sensor("sensor.living_room_temperature", 16).
:-dynamic( light_sensor/2 ).
light_sensor("sensor.outside_light_density", low).
:-dynamic( light_switch/2 ).
light_switch("switch.kitchen_light", on).
light_switch("switch.living_room_light", on).

write_states(X) :-
        	atom_concat(X, '-states.pl', Y),
        	telling(OldStream),
        	tell(Y),
        	listing(X),
        	told,
        	tell(OldStream).

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

