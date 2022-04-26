/*
Samasuguse nimega reegleid ei tohi olla, sest need lähevad konflikti
% dark & window.open -> !light
rule :-
    light_sensor("sensor.outside_light_density", low),
    window_switch("switch.kitchen_window", open),
    light_switch("switch.kitchen_light", off).
*/

/*
%  dark & !window.open -> light
rule(Result1, Result2) :-
    light_sensor("sensor.outside_light_density", low),
    window_switch("switch.kitchen_window", closed, Result1), 
    light_switch("switch.kitchen_light", on, Result2).
*/


%  dark & window.open -> !light
rule :-
    light_sensor("sensor.outside_light_density", low),
    switch_status("switch.kitchen_window", on),
    light_switch("light.kitchen_light_group", off).

%  dark & !window.open -> light
dark_windowClosed_lightOn :-
    light_sensor("sensor.outside_light_density", low),
    switch_status("switch.kitchen_window", off),
    light_switch("light.kitchen_light_group", on).

rule2 :-
    temperature_sensor("sensor.living_room_temperature", medium),
    climate_mode("climate.air_conditioner", heat).


