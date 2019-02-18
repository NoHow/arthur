#!/usr/bin/python3 
import telnetlib as tl
import time
import sys

import tools as tls

host = sys.argv[1]
port = sys.argv[2]
leaf = sys.argv[3]

if switch_name == vd.Switch.ZTE.name.lower():
    print('zte')
    tools.login_try(tn, user, password)
    libr_log.zte_gui_proccessing(tn, HOST, port)
elif switch_name == vd.Switch.LINKSYS.name.lower():
    print('lks')
    tools.login_try(tn, user, password)
    libr_log.linksys_gui_proccessing(tn, HOST, port)
elif switch_name == vd.Switch.RAISECOM.name.lower():
    print('iscom')
    tools.login_try(tn, user, password)
    libr_log.raisecom_gui_proccessing(tn, HOST, port)
elif switch_name == vd.Switch.FOXGATE.name.lower():
    print('fox')
    tools.login_try(tn, user, password)
    libr_log.foxgate_gui_proccessing(tn, HOST, port)
elif switch_name == vd.Switch.DLINK.name.lower():
    print('bdcom')
    tools.login_try(tn, user, password)
    libr_log.dlink_gui_proccessing(tn, HOST, port)
elif switch_name == vd.Switch.BDCOM.name.lower():
    libr_log.bdcom_gui_proccessing(tn, HOST, leaf, port)

tn = tl.Telnet(host)

