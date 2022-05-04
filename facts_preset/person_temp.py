def person_fact(entity_id, entity_attr, file):
    file.write('person_status("' + entity_id + '", ' + entity_attr[0] + ").\n")
    file.write('domain("' + entity_id + '", "person").\n')
