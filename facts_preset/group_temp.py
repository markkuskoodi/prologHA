def group_fact(device_id, device_attr, file):
    entity_group = device_attr[1].get("entity_id")
    for i in entity_group:
        file.write('group("' + i + '", "' + device_id + '").\n')