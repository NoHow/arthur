import time
import re
import urllib.request

import tools
import constants
import snmp_proccessing as sp
import vendors as vd

def get_switch_vendor(mng_ip):
    device_info = None
    device_info = sp.get_vendor(mng_ip)
    if device_info == None:
        return -100

    if re.search("des-3200", device_info, flags=re.I):
        return vd.Switch.DLINK_3200.name
    elif re.search("des-3526", device_info, flags=re.I):
        return vd.Switch.DLINK_3526.name
    elif re.search("zte", device_info, flags=re.I):
        return vd.Switch.ZTE.name
    elif re.search("bdcom", device_info, flags=re.I):
        return vd.Switch.BDCOM.name
    elif re.search("iscom", device_info, flags=re.I):
        return vd.Switch.RAISECOM.name
    elif re.search("Gigabit Switch with CLI and WebView", device_info, flags=re.I):
        return vd.Switch.LINKSYS.name
    elif re.search("foxgate", device_info, flags=re.I):
        return vd.Switch.FOXGATE.name

def get_gateway_vendor(gt_ip):
    device_info = None
    device_info = sp.get_gt_vendor(gt_ip)
    if device_info == None:
        return -100

    if re.search("cisco", device_info, flags=re.I):
        return vd.Gateway.CISCO.name
    elif re.search("zte", device_info, flags=re.I):
        return vd.Gateway.ZTE.name
    elif re.search("huawei", device_info, flags=re.I):
        return vd.Gateway.HUAWEI.name
    elif re.search("juniper", device_info, flags=re.I):
        return vd.Gateway.JUNIPER.name