def sensor_type(device_id, device_attr, file):
    if device_attr[1].get('unit_of_measurement') == '°C':
        temperature_sensor(device_id, device_attr, file)
    elif device_attr[1].get('unit_of_measurement') == 'lm':
        light_sensor(device_id, device_attr, file)


def light_sensor(device_id, device_attr, file):
    file.write('light_sensor("' + device_id + '", ' + "low" + ').\n')
    '''
            if(int(device_attr[0]) < 200):
                file.write('light_sensor("' + i + '", ' + "low" + ').\n')
            elif(int(device_attr[0]) >= 200 and int(device_attr[0]) <= 300):
                file.write('light_sensor("' + i + '", ' + "medium" + ').\n')
            elif(int(device_attr[0]) > 300):
                file.write('light_sensor("' + i + '", ' + "high" + ').\n')
    '''


def temperature_sensor(device_id, device_attr, file):
    if int(device_attr[0]) < 10:
        file.write('temperature_sensor("' + device_id + '", ' + "low" + ').\n')
    elif 10 <= int(device_attr[0]) <= 20:
        file.write('temperature_sensor("' + device_id + '", ' + "medium" + ').\n')
    elif int(device_attr[0]) > 20:
        file.write('temperature_sensor("' + device_id + '", ' + "high" + ').\n')
