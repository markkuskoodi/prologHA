import make_prolog_file


def sensor_type(device_id, device_attr, file):
    if device_attr[1].get('unit_of_measurement') == '°C':
        temperature_sensor(device_id, device_attr, file)
        make_prolog_file.entity_type(device_id, device_attr, file)
    elif device_attr[1].get('unit_of_measurement') == 'lx':
        light_sensor(device_id, device_attr, file)
        make_prolog_file.entity_type(device_id, device_attr, file)


def light_sensor(device_id, device_attr, file):
    if float(device_attr[0]) < 130:
        file.write('light_sensor_status("' + device_id + '", ' + "low" + ').\n')
    elif 130 <= float(device_attr[0]) <= 170:
        file.write('light_sensor_status("' + device_id + '", ' + "medium" + ').\n')
    elif float(device_attr[0]) > 170:
        file.write('light_sensor_status("' + device_id + '", ' + "high" + ').\n')
    file.write('domain("' + device_id + '", "light").\n')


def temperature_sensor(device_id, device_attr, file):
    if float(device_attr[0]) < 10:
        file.write('temperature_sensor_status("' + device_id + '", ' + "low" + ').\n')
    elif 15 <= float(device_attr[0]) <= 22:
        file.write('temperature_sensor_status("' + device_id + '", ' + "medium" + ').\n')
    elif float(device_attr[0]) > 22:
        file.write('temperature_sensor_status("' + device_id + '", ' + "high" + ').\n')
    file.write('domain("' + device_id + '", "temperature").\n')
