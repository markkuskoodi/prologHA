def switch_type(device_id, device_attr, file):
    if "window" in device_id:
        file.write('actuator("' + device_id + '", ' + device_attr[0] + ').\n')
        file.write('domain("' + device_id + '", "switch").\n')
        file.write('actuator_type("' + device_id + '", window).\n')
    elif "curtain" in device_id:
        file.write('actuator("' + device_id + '", ' + device_attr[0] + ').\n')
        file.write('domain("' + device_id + '", "switch").\n')
        file.write('domain("' + device_id + '", "light").\n')
        file.write('actuator_type("' + device_id + '", curtain).\n')
    else:
        file.write('actuator("' + device_id + '", ' + device_attr[0] + ').\n')
        file.write('domain("' + device_id + '", "switch").\n')
        file.write('actuator_type("' + device_id + '", switch).\n')
