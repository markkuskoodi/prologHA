:-style_check(-singleton).

action(light, "increase_light", on).
action(light, "decrease_light", off).
action(switch, "increase_light", on).
action(switch, "decrease_light", off).
action(curtain, "increase_light", up).
action(curtain, "decrease_light", down).

sensor(Device_id, Value):-
	actuator(Device_id, Value).

time_comparison(After_time, Before_time) :-
        process_create(path(python), ["time_comparison.py", After_time, Before_time], [stdout(pipe(Stream)),
                                    stderr(pipe(Stream))]),
        read_string(Stream, Len, Out),
        split_string(Out, "\n", "", Output),
        nth0(1, Output, Result),
        (Result = "true"),
        catch(close(Stream), error(process_error(_,exit(_)), _), true).

group_scope(Group, Result):-
	findall(Entity_id, group(Entity_id, Group), Result).

group_scope(Group, Scope, Result):-
	findall(Entity_id, group(Group_id, Group), GroupScope),
	intersection(Scope, GroupScope, Result).

domain_scope(Domain, Result):-
	findall(Entity_id, domain(Entity_id, Domain), Result).

domain_scope(Domain, Scope, Result):-
	findall(Entity_id, domain(Entity_id, Domain), DomainScope),
	intersection(Scope, DomainScope, Result).

find_actuator_by_goal(Entity_id, Goal, Scope) :-
	actuator(Entity_id, Entity_status),
	actuator_type(Entity_id, Entity_type),
	action(Entity_type, Goal, Entity_status),
	member(Entity_id, Scope).

actuator_state(Entity_id, State):-
	actuator_type(Entity_id, Entity_type),
	action(Entity_type, State, Action),
    actuator(Entity_id, Action),!.
actuator_state(Entity_id, State):-
	actuator_type(Entity_id, Entity_type),
	action(Entity_type, State, Action),
    \+ actuator(Entity_id, Action),
    actuator_action(Entity_id, Action),!.

actuator_action(Entity_id, Action):-
    string_concat(Entity_id, " ", TempResp),
    string_concat(TempResp, Action, TempResp_2),
    string_concat(TempResp_2, "\n", Response),
    write_output(Response).

actuator_action(Entity_id, Action, Mode):-
    string_concat(Entity_id, " ", TempResp),
    string_concat(TempResp, Action, TempResp_2),
    string_concat(TempResp_2, " ", TempResp_3),
    string_concat(TempResp_3, Mode, TempResp_4),
    string_concat(TempResp_4, "\n", Response),
    write_output(Response).
/*
	Kui automatsiooni eesmärgiks on vähendada valgus taset kasutades skoobis olevaid seadmeid. Workflow on järgmine:
		1. Vaatame kas valgussensori tase ei ole madal
		2. Otsime aktuaatori mille eesmärk on eelnevalt olnud valgustaseme tõstmine
		4. Vähendame valgustaset eelmises punktis võetud seadmega.
*/
light_sensor(Entity_id, low, Scope) :-
	\+ light_sensor_status(Entity_id, low),
	% Otsime ühe aktuaatori mille eesmärk oli valguse suurendamine ning mis on skoobis olemas
	find_actuator_by_goal(Actuator_id, "increase_light", Scope),
	% Lülitame välja leitud töötava aktuaatori, et valgus taset vähendada
	actuator_state(Actuator_id, "decrease_light"),!.

/*
	Kui automatsiooni eesmärgiks on suurendada ruumi valgus taset. Workflow on järgmine:
		1. Vaatame kas valgussensori tase ei ole madal
		2. Otsime aktuaatori mille eesmärk on eelnevalt olnud valgustaseme langetamine
		4. Vähendame valgustaset eelmises punktis võetud seadmega.
*/
light_sensor(Entity_id, high, Scope) :-
	\+ light_sensor_status(Entity_id, high),
	% Otsime mittetöötavad aktuaator
	find_actuator_by_goal(Actuator_id, "decrease_light", Scope),
	% Lülitame sisse, et valgus taset suurendada
	actuator_state(Actuator_id, "increase_light"),!.