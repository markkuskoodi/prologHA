import json

def rawData(data):
    data_temp = json.loads(data)
    result = data_temp.get("result")

    data = {}

    for i in result:
        if(i.get("entity_id").startswith('sensor')):
            data[i.get("entity_id")] = (i.get("state"), i.get("attributes"))
        if(i.get("entity_id").startswith('switch')):
            data[i.get("entity_id")] = (i.get("state"))

    return data

def getIdAndState(line):
    temp = line.split('(')[1].split(')')[0].split(',')
    return temp[0].strip('"'), 'turn_' + temp[1].strip()
    