from snmp_cmds import snmpwalk

result = snmpwalk(community='74FRfR7ewJar',
                  ipaddress='172.17.217.17',
                  oid='iso.3.6.1.2.1.1.1.0')
                  
print(result[0][1])