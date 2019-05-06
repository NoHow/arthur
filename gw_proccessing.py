import tools as tls
import underground as ug
import telnetlib as tl
import vendors as vd
import re
import time
import snmp_cmds as sc

def get_connection(sw_ip):
    first_octets = re.search(r"(\d{1,3}[.]){3}", sw_ip).group()
    gw_ip = first_octets + "1"

    try:
        vendor = ug.get_gateway_vendor(gw_ip)

        user = "blankuser"
        password = "blankpassword"
        if vendor == vd.Gateway.CISCO.name:
            user = "blankuser"
            password = "blankpassword"
        elif vendor == vd.Gateway.ZTE.name or vendor == vd.Gateway.JUNIPER.name:
            user = "blankuser"
            password = "blankpassword"
        elif vendor == vd.Gateway.HUAWEI.name:
            user = "blankuser"
            password = "blankpassword"
        
        tn_gw = tl.Telnet(gw_ip)
        tls.login_try(tn_gw, user, password)

        return {'connection' : tn_gw, 'vendor' : vendor}
    except (sc.exceptions.SNMPError, sc.exceptions.SNMPTimeout):

        return {'connection' : None, 'vendor' : None}




def show_arp_by_mac(tn_gw, vendor, mac):
    tmac = tls.transform_mac(mac)

    if vendor == vd.Gateway.CISCO.name:
        tls.send_taska(tn_gw, "show arp | include " + tmac, 'default', 2)
        return 1
    elif vendor == vd.Gateway.ZTE.name:
        tls.send_taska(tn_gw, "show arp dynamic | include " + tmac, 'default', 2)
        return 1
    elif vendor == vd.Gateway.JUNIPER.name:
        jmac = tls.transform_mac_2p(tmac)
        tls.send_taska(tn_gw, "show arp | match " + jmac, 'default', 2)
        return 1
    elif vendor == vd.Gateway.HUAWEI.name:
        hmac = tls.transform_mac_def(tmac)
        tls.send_taska(tn_gw, "display arp dynamic | include " + hmac, 'default', 2)
        return 1

    return -1

def show_ring(tn_gw, vendor, sw_ip):
    ring_ip = re.search(r"(\d{1,3}[.]){3}", sw_ip).group()

    if vendor == vd.Gateway.CISCO.name:
        tls.send_taska(tn_gw, "show arp | include " + ring_ip, 'default', 2)
    elif vendor == vd.Gateway.ZTE.name:
        tls.send_taska(tn_gw, "show arp dynamic | include " + ring_ip, 'default', 2)
    elif vendor == vd.Gateway.JUNIPER.name:
        tls.send_taska(tn_gw, "show arp | match " + ring_ip, 'default', 2)
    elif vendor == vd.Gateway.HUAWEI.name:
        tls.send_taska(tn_gw, "display arp dynamic | include " + ring_ip, 'default', 2)

    for i in range(3):
        time.sleep(0.1)
        tls.send_taska(tn_gw, " ")
    
    return 1

def show_abon_mac(tn_gw, vendor, mac):
    tmac = tls.transform_mac(mac)

    if vendor == vd.Gateway.CISCO.name:
        tls.send_taska(tn_gw, "show mac address-table address " + tmac, 'default', 2)
        return 1
    elif vendor == vd.Gateway.ZTE.name:
        tls.send_taska(tn_gw, "show mac " + tmac, 'default', 2)
        return 1
    elif vendor == vd.Gateway.JUNIPER.name:
        jmac = tls.transform_mac_2p(tmac)
        tls.send_taska(tn_gw, "show bridge mac-table " + jmac, 'default', 2)
        return 1
    elif vendor == vd.Gateway.HUAWEI.name:
        hmac = tls.transform_mac_def(tmac)
        tls.send_taska(tn_gw, "display mac-address " + hmac, 'default', 2)
        return 1

    return -1
