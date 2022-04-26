def light_fact(device_id, device_attr, file):
    file.write('light_status("' + device_id + '", ' + device_attr[0] + ').\n')
