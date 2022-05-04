def light_fact(device_id, device_attr, file):
    file.write('actuator("' + device_id + '", ' + device_attr[0] + ').\n')
    file.write('domain("' + device_id + '", "light").\n')
    file.write('actuator_type("' + device_id + '", light).\n')
