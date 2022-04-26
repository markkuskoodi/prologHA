def climate_fact(device_id, device_attr, file):
    if "boiler" in device_id:
        file.write('climate_mode_status("' + device_id + '", ' + device_attr[0] + ').\n')
        file.write('climate_temperature_status("' + device_id + '", ' + str(device_attr[1].get("temperature")) + ').\n')
    else:
        file.write('climate_mode_status("' + device_id + '", ' + device_attr[0] + ').\n')
        file.write('climate_temperature_status("' + device_id + '", ' + str(device_attr[1].get("temperature")) + ').\n')
        file.write('climate_fan_status("' + device_id + '", ' + device_attr[1].get("fan_mode") + ').\n')
        file.write('climate_swing_status("' + device_id + '", ' + device_attr[1].get("swing_mode") + ').\n')

