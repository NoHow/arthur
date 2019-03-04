import switch_proc as sp
import telnetlib as tl
import time
import tools as tls
import threading

tn_sw = tl.Telnet("192.168.0.1")
sw_ip = "192.168.0.1"
port = 1
leaf = 2

tn_sw.write("admin".encode('ascii') + b"\r")
time.sleep(1)
tn_sw.write("322228oda".encode('ascii') + b"\r")


#VISUAL TESTS
#sp.zte_init(tn_sw, sw_ip, port)
#sp.cisco_init(tn_sw, sw_ip, port)
#sp.dlink_3200_init(tn_sw, sw_ip, port)
#sp.dlink_3526_init(tn_sw, sw_ip, port)
#sp.foxgate_init(tn_sw, sw_ip, port)
#sp.bdcom_init(tn_sw, sw_ip, leaf, port)

def output_testing(tn_sw):
    answer = tls.AsyncOutput(tn_sw)
    answer.start()
    
    for i in range(99):
        tls.send_taska(tn_sw, "help")

    answer.tryharding = 0
    tls.send_task(tn_sw, "logout")

output_testing(tn_sw)

tn_sw.write("logout".encode('ascii') + b"\r")