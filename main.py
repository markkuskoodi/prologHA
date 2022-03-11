from webhook import Webhook
from pyswip import Prolog
import rawdata
import os

hook = Webhook()

data = rawdata.rawData(hook.get_states())

predicate = []
switch_states = []
sensor_states = []

with open("test3.pl", 'w') as file:
    for i in data:
        if(i.startswith('sensor')):
            temp = data.get(i)
            if(temp[1].get('unit_of_measurement') == '°C'):
                if('temperature_sensor' not in sensor_states):
                    sensor_states.append('temperature_sensor')
                    file.write(':-dynamic( temperature_sensor/2 ).\n')
                file.write('temperature_sensor("' + i + '", ' + temp[0] + ').\n')
            elif(temp[1].get('unit_of_measurement') == 'lm'):
                if('light_sensor' not in sensor_states):
                    sensor_states.append('light_sensor')
                    file.write(':-dynamic( light_sensor/2 ).\n')
                file.write('light_sensor("' + i + '", ' + "low" + ').\n')
        elif(i.startswith('switch')):
            temp = data.get(i)
            if(i.endswith('_light')):
                if('light_switch' not in switch_states):
                    switch_states.append('light_switch')
                    file.write(':-dynamic( light_switch/2 ).\n')
                file.write('light_switch("' + i + '", ' + temp + ').\n')
    
    file.write("\nwrite_states(X) :-\n\
        \tatom_concat(X, '-states.pl', Y),\n\
        \ttelling(OldStream),\n\
        \ttell(Y),\n\
        \tlisting(X),\n\
        \ttold,\n\
        \ttell(OldStream).\n\n")
    
    #TODO Iga reegli puhul checkida, et kas selline seade on olemas.
    with open('ac_automation(usual).pro', 'r') as automation:
        lines = automation.readlines()
        for i in lines:
            if(i.strip().endswith(":-")):
                predicate.append(i.strip().split(":-")[0].strip())
            file.write(i)
    
prolog = Prolog()
prolog.consult("test3.pl")

for i in predicate:
    for res in prolog.query(i):
        print(res)

for i in switch_states:
    for res in prolog.query("write_states(" + i + ")"):
        print(res)

files = [filename for filename in os.listdir(".") if filename.endswith('-states.pl')]

for i in files:
    with open(i, "r") as file:
        lines = file.readlines()
        know_states = i.split("-")[0]
        for i in lines:
            temp = i.strip()
            if(temp.startswith(know_states)):
                if(temp.startswith("light") and "sensor" not in temp):
                    entity_id, state = rawdata.getIdAndState(temp)
                    hook.send_state(entity_id, state)
                                   

