#!/bin/bash
echo "Start makerbase-client"
time=$(date "+%Y%m%d%H%M%S")
# /root/makerbase-client/build/MakerbaseClient localhost > /root/mksclient/test-$time.log
/home/biqu/Desktop/myfile/znp/znp_tjc_klipper/build/io -4 0xff100028 0x010000
#sleep 4
/home/biqu/Desktop/myfile/znp/znp_tjc_klipper/build/znp_tjc_klipper localhost >/dev/null 2>&1
