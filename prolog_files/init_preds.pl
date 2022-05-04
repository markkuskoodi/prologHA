:-style_check(-singleton).

action(light, "increase_light", on).
action(light, "decrease_light", off).
action(switch, "increase_light", on).
action(switch, "decrease_light", off).
action(curtain, "increase_light", up).
action(curtain, "decrease_light", down).

sensor(Device_id, Value):-
	actuator(Device_id, Value).

check_entity_type(X, Y):-
    entity_type(X, Y).

time_comparison(After_time, Before_time) :-
        process_create(path(python), ["time_comparison.py", After_time, Before_time], [stdout(pipe(Stream)),
                                    stderr(pipe(Stream))]),
        read_string(Stream, Len, Out),
        split_string(Out, "\n", "", Output),
        nth0(1, Output, Result),
        (Result = "true"),
        catch(close(Stream), error(process_error(_,exit(_)), _), true).

group_scope(Room, Result):-
	findall(X, group(X, Room), Result).

group_scope(Room, Scope, Result):-
	findall(X, group(X, Room), GroupScope),
	intersection(Scope, GroupScope, Result).

domain_scope(Domain, Result):-
	findall(X, domain(X, Domain), Result).

domain_scope(Domain, Scope, Result):-
	findall(X, domain(X, Domain), DomainScope),
	intersection(Scope, DomainScope, Result).

% Filtreerime aktuaatoreid eesmärgi järgi
find_actuator_by_goal(Device_id, Goal, Scope) :-
	actuator(Device_id, Device_status),
	actuator_type(Device_id, Device_type),
	action(Device_type, Goal, Device_status),
	member(Device_id, Scope).

actuator_action(Device_id, Status):-
	actuator_type(Device_id, Device_type),
	action(Device_type, Status, Action),
    actuator(Device_id, Action),!.
actuator_action(Device_id, Status):-
	actuator_type(Device_id, Device_type),
	action(Device_type, Status, Action),
    \+ actuator(Device_id, Action),
    rule_output(Device_id, Action),!.

rule_output(Device_id, Action):-
    string_concat(Device_id, " ", TempResp),
    string_concat(TempResp, Action, TempResp_2),
    string_concat(TempResp_2, "\n", Response),
    write_output(Response).

/*
	Kui automatsiooni eesmärgiks on vähendada ruumi valgus taset. Workflow on järgmine:
		1. Vaatame kas valgussensori tase ei ole madal
		2. Otsime seadmed mille eesmärk on eelnevalt olnud valgustaseme tõstmine
		3. Võtame ühe seadme eelmises punktis leitu põhjal
		4. Vähendame valgustaset eelmises punktis võetud seadmega.
*/
light_sensor(Device_id, low, Scope) :-
	\+ light_sensor_status(Device_id, low),
	% Otsime ühe aktuaatori mille eesmärk oli valguse suurendamine ning mis on skoobis olemas
	find_actuator_by_goal(Light_id, "increase_light", Scope),
	% Lülitame välja leitud töötava aktuaatori, et valgus taset vähendada
	actuator_action(Light_id, "decrease_light"),!.

/*
	Kui automatsiooni eesmärgiks on suurendada ruumi valgus taset. Workflow on järgmine:
		1. Vaatame kas valgussensori tase ei ole madal
		2. Otsime seadmed mille eesmärk on eelnevalt olnud valgustaseme tõstmine
		3. Võtame ühe seadme eelmises punktis leitu põhjal
		4. Vähendame valgustaset eelmises punktis võetud seadmega.
*/
light_sensor(Device_id, high, Scope) :-
	\+ light_sensor_status(Device_id, high),
	% Otsime mittetöötavad aktuaator
	find_actuator_by_goal(Light_id, "decrease_light", Scope),
	% Lülitame sisse, et valgus taset suurendada
	actuator_action(Light_id, "increase_light"),!.