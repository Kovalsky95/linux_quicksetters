#adb -s 0123456789ABCDEF tcpip 5555
#adb -s 192.168.0.4:5555 tcpip 5555
#scrcpy -s 0123456789ABCDEF
scrcpy-noconsole -s 192.168.0.4:5555
