from facts_preset.sensor_temp import sensor_type
from facts_preset.switch_temp import switch_type
from facts_preset.climate_temp import climate_fact
from facts_preset.light_temp import light_fact
from facts_preset.person_temp import person_fact
from facts_preset.group_temp import group_fact

"""
Funktsioon mis loeb sisse kõik Home-Assistant poolt saadetud seadmed ning kirjutab need faktidena prolog_invokeri
lõpp faili mida hiljem kasutatakse automatsioonide kohta pärimiseks.
#TODO Juurde lisada faktide support teiste seadmete jaoks. Lisaks gruppide põhine faktide süsteem. Lisaks teha mingi universaalne
confi fail, et saaks ära kaotada selle koleda if-de rägastiku.
"""


def add_facts(data, file, log_file_name):
    for device_id in data:
        device_attr = data.get(device_id)
        if device_attr[0] == "unavailable" or device_attr[0] == "unknown":
            with open("logs/" + log_file_name, 'a') as log:
                log.write(device_id + ": " + device_attr[0] + "\n")
        elif device_id.startswith('sensor.'):
            sensor_type(device_id, device_attr, file)
        elif device_id.startswith('switch.'):
            switch_type(device_id, device_attr, file)
            entity_type(device_id, device_attr, file)
        elif device_id.startswith('climate.'):
            climate_fact(device_id, device_attr, file)
            entity_type(device_id, device_attr, file)
        elif device_id.startswith('light.'):
            light_fact(device_id, device_attr, file)
            entity_type(device_id, device_attr, file)
        elif device_id.startswith('person.'):
            person_fact(device_id, device_attr, file)
            entity_type(device_id, device_attr, file)
        elif device_id.startswith('group.'):
            group_fact(device_id, device_attr, file)
            entity_type(device_id, device_attr, file)

    file.write('\n')


'''
See funktsioon lisab faili mida prolog_invoker kasutab minu poolt tehtud Prolog reeglid täiturite (switchid, AC-d jne) kohta,
mida hiljem lõpp-kasutaja automatsiooni reeglite koostamisel peab kasutama. 
'''


# TODO Lisada veel Prologi täitureid mida kasutaja veel kasutada võib. Prolog side grupipõhine support.

def add_init_preds(file, result_file_name):
    with open('init_preds.pl', 'r') as preds:
        lines = preds.readlines()
        for i in lines:
            if "<insert_result_name>" in i:
                file.write("\topen('" + result_file_name + "', append, Out),\n")
            else:
                file.write(i)

    file.write('\n')


'''
See on funktsioon, mis loeb sisse kõik kasutajate poolt tehtud reeglid prologis ja kirjutab need faili mida hiljem
prolog_invoker kasutab. Funktsioon lisab kõik reeglite päised predicate massiivi, et hiljem prolog_invoker saaks 
teha päringuid kasutaja poolt loodud reeglite pihta. Lisaks funktsioon kontrollib kas kasutaja poolt kirjutatud reeglites
on seadmete ID-d õiged ning täiturite predikaatidele lisab veel Result muutuja, sest prolog_invoker hakkab väljastamiseks
kasutama Result muutujat.                                                                                                                                                                  
#TODO Proovida lahti saada code-smellist. Not sure kuidas veel, sest kõik on stringi põhine ning see if-de rägastik siin 
on vajalik.
'''


def get_users_rules(data):
    predicate = []
    comment = False
    #with open('prolog_files/multiple_rules_exec_test.pl', 'r') as automation:
    with open('prolog_files/automation_rules.pl', 'r') as automation:
        lines = automation.readlines()
        for i in lines:
            line = i.strip()
            if line.endswith(":-") and comment is False and '(' not in line:
                pred = line.split(" :-")
                if pred[0] + "." not in predicate:
                    predicate.append(pred[0] + ".")
            else:
                if (not (line.startswith("%")) and line != "" and not (line.startswith("/*")) and not (
                        line.startswith('*/')) and comment is False):
                    rule_name = line.split("(")[0]
                    if rule_name in "actuator" or "sensor" in rule_name:
                        device_id = line.split("(")[1].split(",")[0]
                        if '"' in device_id and ":" not in device_id:
                            device_id = device_id.strip('"')
                            if device_id not in data:
                                raise Exception("This device doesn't exist")
                    else:
                        continue
                elif line.startswith("/*") and comment is False:
                    comment = True
                elif line.startswith("*/") and comment is True:
                    comment = False
    return predicate


def entity_type(device_id, device_attr, file):
    if device_attr[1].get("entity_id") is None and device_attr[1].get("is_hue_group") is not True:
        file.write('entity_type("' + device_id + '", single).\n')
    else:
        file.write('entity_type("' + device_id + '", group).\n')
