light_switch(Device_id, Status):-
    light_status(Device_id, Status),!.
light_switch(Device_id, Status):-
    \+ light_status(Device_id, Status),
    string_concat(Device_id, " ", TempResp),
    string_concat(TempResp, Status, TempResp_2),
    string_concat(TempResp_2, "\n", Response),
    write_output(Response),!.

window_switch(Device_id, Status):-
    window_status(Device_id, Status),!.
window_switch(Device_id, Status):-
    \+ window_status(Device_id, Status),
    string_concat(Device_id, " ", TempResp),
    string_concat(TempResp, Status, TempResp_2),
    string_concat(TempResp_2, "\n", Response),
    write_output(Response),!.

climate_mode(Device_id, Mode):-
    climate_mode_status(Device_id, Mode),!.
climate_mode(Device_id, Mode):-
    \+ climate_mode_status(Device_id, Mode),
    string_concat(Device_id, " ", TempResp),
    string_concat(TempResp, Mode, TempResp_2),
    string_concat(TempResp_2, " mode\n", Response),
    write_output(Response),!.

climate_temperature(Device_id, Temp):-
    climate_temperature_status(Device_id, Temp),!.
climate_temperature(Device_id, Temp):-
    \+ climate_temperature_status(Device_id, Temp),
    string_concat(Device_id, " ", TempResp),
    string_concat(TempResp, Temp, TempResp_2),
    string_concat(TempResp_2, " temperature\n", Response),
    write_output(Response),!.

climate_fan(Device_id, Fan):-
    climate_fan_status(Device_id, Fan),!.
climate_fan(Device_id, Fan):-
    \+ climate_fan_status(Device_id, Fan),
    string_concat(Device_id, " ", TempResp),
    string_concat(TempResp, Fan, TempResp_2),
    string_concat(TempResp_2, " fan_mode\n", Response),
    write_output(Response),!.

climate_swing(Device_id, Swing_status):-
    climate_swing_status(Device_id, Swing_status),!.
climate_swing(Device_id, Swing_status):-
    \+ climate_swing_status(Device_id, Swing_status),
    string_concat(Device_id, " ", TempResp),
    string_concat(TempResp, Swing_status, TempResp_2),
    string_concat(TempResp_2, " swing\n", Response),
    write_output(Response),!.