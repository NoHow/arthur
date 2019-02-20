#!/usr/bin/python3 
import telnetlib as tl
import time
import sys

import tools as tls
import switch_proc as swp
import underground as ug
import vendors as vd

host = sys.argv[1]
port = sys.argv[2]

if len(sys.argv) == 4:
    leaf = sys.argv[3]

switch_name = ug.get_switch_vendor(host)
tn_sw = tl.Telnet(host)

if switch_name == vd.Switch.ZTE.name:
    swp.zte_init(tn_sw, host, port)
elif switch_name == vd.Switch.LINKSYS.name:
    swp.zte_init(tn_sw, host, port)
elif switch_name == vd.Switch.RAISECOM.name:
    pass
elif switch_name == vd.Switch.FOXGATE.name:
    pass
elif switch_name == vd.Switch.DLINK_3200.name:
    swp.dlink_3200_init(tn_sw, host, port)
elif switch_name == vd.Switch.DLINK_3526.name:
    swp.dlink_3526_init(tn_sw, host, port)
elif switch_name == vd.Switch.BDCOM.name:
    swp.bdcom_init(tn_sw, host, leaf, port)

tn_sw.close()
