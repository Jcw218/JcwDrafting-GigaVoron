#!/usr/bin/env python2
# Tool to reset canbus_uuid
import sys, os
def modify_config(file_path, new_uuid):
    if not os.path.exists(file_path):
        sys.stdout.write("File path does not exist: {}".format(file_path))
        return
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith('canbus_uuid:'):
                line = 'canbus_uuid: ' + new_uuid + '\n'
            file.write(line)

uuid_list=['000000000000','000000000000','000000000000','000000000000']
for i, uuid in enumerate(uuid_list):
    if uuid != '':
        config_path = "/home/biqu/printer_data/config/znp_thr{}.cfg".format(i+1)
        modify_config(config_path, uuid)
        sys.stdout.write("set canbus_uuid:%s into %s\n"% (uuid, config_path))
modify_config("/home/biqu/printer_data/config/znp_mcu.cfg", "000000000000")
