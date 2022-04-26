def switch_type(device_id, device_attr, file):
    file.write('switch_status("' + device_id + '", ' + device_attr[0] + ').\n')
