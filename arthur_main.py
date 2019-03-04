#! python3
import telnetlib as tl
import time
import sys

import tools as tls
import switch_proc as swp
import underground as ug
import vendors as vd


host = sys.argv[1]

switch_name = ug.get_switch_vendor(host)
tn_sw = tl.Telnet(host)

if switch_name == vd.Switch.ZTE.name:
    port = input("Port: ")
    swp.zte_init(tn_sw, host, port)
elif switch_name == vd.Switch.LINKSYS.name:
    port = input("Port: ")
    swp.cisco_init(tn_sw, host, port)
elif switch_name == vd.Switch.RAISECOM.name:
    port = input("Port: ")
    swp.raisecom_init(tn_sw, host, port)
elif switch_name == vd.Switch.FOXGATE.name:
    print('Sorry, no raisecom right now!')
    #port = input("Port: ")
    #swp.foxgate_init(tn_sw, host, port)
elif switch_name == vd.Switch.DLINK_3200.name:
    port = input("Port: ")
    swp.dlink_3200_init(tn_sw, host, port)
elif switch_name == vd.Switch.DLINK_3526.name:
    port = input("Port: ")
    swp.dlink_3526_init(tn_sw, host, port)
elif switch_name == vd.Switch.BDCOM.name:
    leaf = input("Leaf: ")
    onu = input("Onu: ")
    swp.bdcom_init(tn_sw, host, leaf, onu)
else:
    print("Sorry, I dont know this device right now!")

tn_sw.close()
