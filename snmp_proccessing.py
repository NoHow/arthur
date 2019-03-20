from snmp_cmds import snmpwalk

def get_vendor(device_ip):
    result = snmpwalk(community='74FRfR7ewJar',
                  ipaddress=device_ip,
                  oid='iso.3.6.1.2.1.1.1.0')
    return result[0][1]

def get_gt_vendor(device_ip):
    result = snmpwalk(community='Ssgp17ifWk',
                ipaddress=device_ip,
                oid='iso.3.6.1.2.1.1.1.0')
    return result[0][1]



    