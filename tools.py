import time
import re
import vendors as vd

DEBUG = 1

def send_task(telnet_inst, task):
    telnet_inst.write(b"\r\n" + task.encode('ascii') + b"\r\n")
    time.sleep(0.1)

def send_taska(telnet_inst, task, sleep_time = 0.5, vendor = 'default'):
    debug_log('task: ' + task)
    debug_log('vendor: ' + vendor)
    if vendor == vd.Switch.RAISECOM.name:
        print('hi!')
        telnet_inst.write(task.encode('ascii') + b"\r")
    elif vendor == 'default':
        telnet_inst.write(b"\r\n" + task.encode('ascii') + b"\r\n")
    time.sleep(sleep_time)
    tmp_answer =  telnet_inst.read_very_eager().decode()
    tmp_answer = re.sub(task, "", tmp_answer)
    answer = tmp_answer

    assure = 1
    try_count = 0
    while assure:
        if try_count > 32:
            assure = 0
        time.sleep(sleep_time)
        tmp_answer = tmp_answer + telnet_inst.read_very_eager().decode()
        if answer != tmp_answer:
            answer = tmp_answer
        elif answer == tmp_answer:
            assure = 0
        try_count = try_count + 1

    debug_log('answer: ' + answer)

    return answer

def clear_garbage(telnet_inst, sleep_time = 0.5):
    time.sleep(sleep_time)
    answer = telnet_inst.read_very_eager().decode()
    print('garbage - ' + answer)

def login_try(telnet_inst, user, password, sleep_time = 0.2):
    telnet_inst.write(user.encode('ascii') + b"\r")
    time.sleep(sleep_time)
    telnet_inst.write(password.encode('ascii') + b"\r")

def transform_mac(original_mac):
    original_mac = original_mac.lower()
    alpha_num_mac = ""
    for c in original_mac:
        if c.isalnum():
            alpha_num_mac = alpha_num_mac + c
    
    i = 0
    new_mac = ""
    for c in alpha_num_mac:
        if i % 4 == 0 and i != 0:
            new_mac = new_mac + '.'
        new_mac = new_mac + c
        i = i + 1
    
    return new_mac

def transform_mac_def(original_mac):
    original_mac = original_mac.lower()
    alpha_num_mac = ""
    for c in original_mac:
        if c.isalnum():
            alpha_num_mac = alpha_num_mac + c
    
    i = 0
    new_mac = ""
    for c in alpha_num_mac:
        if i % 4 == 0 and i != 0:
            new_mac = new_mac + '-'
        new_mac = new_mac + c
        i = i + 1
    
    return new_mac

def transform_mac_2p(original_mac):
    original_mac = original_mac.lower()
    alpha_num_mac = ""
    for c in original_mac:
        if c.isalnum():
            alpha_num_mac = alpha_num_mac + c

    i = 0
    new_mac = ""
    for c in alpha_num_mac:
        if i % 2 == 0 and i != 0:
            new_mac = new_mac + ':'
        new_mac = new_mac + c
        i = i + 1
    
    return new_mac

def debug_log(verbose_data):
    if DEBUG:
        print (verbose_data)
    elif DEBUG == 0:
        pass
    return