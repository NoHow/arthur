import switch_proc as sp
import telnetlib as tl
import time
import tools as tls
import threading

tn_sw = tl.Telnet("172.17.34.51")
sw_ip = "172.17.34.51"
port = 1
leaf = 2

tn_sw.set_debuglevel(0)
sp.zte_init(tn_sw, sw_ip, 1)

tn_sw.close()