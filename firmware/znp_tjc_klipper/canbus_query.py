#!/usr/bin/env python2
# Tool to query CAN bus uuids
#
# Copyright (C) 2021  Kevin O'Connor <kevin@koconnor.net>
#
# This file may be distributed under the terms of the GNU GPLv3 license.
import sys, os, optparse, time
import can

CANBUS_ID_ADMIN = 0x3f0
CMD_QUERY_UNASSIGNED = 0x00
RESP_NEED_NODEID = 0x20
CMD_SET_KLIPPER_NODEID = 0x01
CMD_SET_KATAPULT_NODEID = 0x11

def query_unassigned(canbus_iface):
    # Open CAN socket
    filters = [{"can_id": CANBUS_ID_ADMIN + 1, "can_mask": 0x7ff,
                "extended": False}]
    bus = can.interface.Bus(channel=canbus_iface, can_filters=filters,
                            bustype='socketcan')
    # Send query
    msg = can.Message(arbitration_id=CANBUS_ID_ADMIN,
                      data=[CMD_QUERY_UNASSIGNED], is_extended_id=False)
    bus.send(msg)
    # Read responses
    found_ids = {}
    uuid_list = []
    start_time = curtime = time.time()
    while 1:
        tdiff = start_time + 2. - curtime
        if tdiff <= 0.:
            break
        msg = bus.recv(tdiff)
        curtime = time.time()
        if (msg is None or msg.arbitration_id != CANBUS_ID_ADMIN + 1
            or msg.dlc < 7 or msg.data[0] != RESP_NEED_NODEID):
            continue
        uuid = sum([v << ((5-i)*8) for i, v in enumerate(msg.data[1:7])])
        cfg_path = set_cfg_path('%012x' % uuid) #Will uuid After converting to a string, it is passed to the judgment function and the corresponding configuration file path is returned.
        sys.stdout.write("%s\n"% (cfg_path))
        if cfg_path:
            modify_config(cfg_path,'%012x' % uuid) #Will uuid Change to the corresponding configuration file
        else:
            uuid_list.append('%012x' % uuid)
        if uuid in found_ids:
            continue
        found_ids[uuid] = 1
        AppNames = {
            CMD_SET_KLIPPER_NODEID: "Klipper",
            CMD_SET_KATAPULT_NODEID: "Katapult"
        }
        app_id = CMD_SET_KLIPPER_NODEID
        if msg.dlc > 7:
            app_id = msg.data[7]
        app_name = AppNames.get(app_id, "Unknown")
        sys.stdout.write("Found canbus_uuid=%012x, Application: %s\n"
                         % (uuid, app_name))
    sys.stdout.write("uuid_list:%s\n" % (uuid_list))
    set_thr_uuid(sorted(uuid_list, key=lambda id: id[-2:]))
    sys.stdout.write("Total %d uuids found\n" % (len(found_ids,)))
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
def set_cfg_path(uuid):
    if uuid[10:12] in ['00', '01', '02', '03']:
        return ""
    else:
        return "/home/biqu/printer_data/config/znp_mcu.cfg"
def set_thr_uuid(uuid_list):
    for i, uuid in enumerate(uuid_list):
        if uuid != '':
            config_path = "/home/biqu/printer_data/config/znp_thr{}.cfg".format(i+1)
            modify_config(config_path, uuid)
            sys.stdout.write("set canbus_uuid:%s into %s\n"% (uuid, config_path))

def main():
    usage = "%prog [options] <can interface>"
    opts = optparse.OptionParser(usage)
    options, args = opts.parse_args()
    if len(args) != 1:
        opts.error("Incorrect number of arguments")
    canbus_iface = args[0]
    query_unassigned(canbus_iface)

if __name__ == '__main__':
    main()
