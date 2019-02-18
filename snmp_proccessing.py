from easysnmp import Session

def get_vendor(device_ip):
    session = Session(hostname=device_ip, community='74FRfR7ewJar', version=1)
    result = session.get('iso.3.6.1.2.1.1.1.0')
    return result.value

def get_gt_vendor(device_ip):
    session = Session(hostname=device_ip, community='Ssgp17ifWk', version=1)
    result = session.get('iso.3.6.1.2.1.1.1.0')
    return result.value