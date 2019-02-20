import switch_proc as sp
import telnetlib as tl

tn_sw = tl.Telnet("192.168.0.1")
sw_ip = "192.168.0.1"
port = 1
leaf = 2

#VISUAL TESTS
#sp.zte_init(tn_sw, sw_ip, port)
#sp.cisco_init(tn_sw, sw_ip, port)
#sp.dlink_3200_init(tn_sw, sw_ip, port)
#sp.dlink_3526_init(tn_sw, sw_ip, port)
#sp.bdcom_init(tn_sw, sw_ip, leaf, port)