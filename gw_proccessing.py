import tools as tls
import underground as ug
import telnetlib as tl
import vendors as vd
import re

def get_connection(sw_ip):
    first_octets = re.search(r"(\d{1,3}[.]){3}", sw_ip).group()
    gw_ip = first_octets + "1"
    vendor = ug.get_gateway_vendor(gw_ip)

    if vendor == vd.Gateway.CISCO.name:
        user = "support"
        password = "ytyfljkf[vfnbnm,f,eire"
    elif vendor == vd.Gateway.ZTE.name or vendor == vd.Gateway.JUNIPER.name:
        user = "duty"
        password = "support"
    elif vendor == vd.Gateway.HUAWEI.name:
        user = "duty"
        password = "support1"
    
    tn_gw = tl.Telnet(gw_ip)
    tls.login_try(tn_gw, user, password)

    return {'connection' : tn_gw, 'vendor' : vendor}

def show_arp_by_mac(tn_gw, vendor, mac):
    tmac = tls.transform_mac(mac)

    if vendor == vd.Gateway.CISCO.name:
        tls.send_taska(tn_gw, "show arp | include " + tmac)
        return 1
    elif vendor == vd.Gateway.ZTE.name:
        tls.send_taska(tn_gw, "show arp dynamic | include " + tmac)
        return 1
    elif vendor == vd.Gateway.JUNIPER.name:
        jmac = tls.transform_mac_2p(tmac)
        tls.send_taska(tn_gw, "show arp | match " + jmac)
        return 1
    elif vendor == vd.Gateway.HUAWEI.name:
        hmac = tls.transform_mac_def(tmac)
        tls.send_taska(tn_gw, "display arp dynamic | include " + hmac)
        return 1

    return -1

