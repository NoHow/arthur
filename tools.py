import time
import re
import vendors as vd
import threading
import sys
import tkinter

DEBUG = 0

class AsyncOutput(threading.Thread):
    def __init__(self, tl_ref):
        threading.Thread.__init__(self)
        self.tl_ref = tl_ref
        self.tryharding = 1

    def run(self):
        while self.tryharding:
            try:
                text = self.tl_ref.read_some()
                if text:
                    sys.stdout.write(text.decode('ascii'))
                    sys.stdout.flush()
            except (ConnectionResetError, ConnectionAbortedError):
                self.tryharding = 0
                print('connection closed')

class AsyncOutputIn(threading.Thread):
    def __init__(self, tl_ref, obox):
        threading.Thread.__init__(self)
        self.tl_ref = tl_ref
        self.tryharding = 1
        self.obox = obox
        self.ftext = ''

    def run(self):
        while 1:
            text = self.tl_ref.read_some()
            if self.tryharding:
                ftext = self.data_processing_for_gui(text.decode('ascii'))
                #sys.stdout.write(text.decode('ascii'))
                #sys.stdout.flush()
                print(repr(ftext))
                self.obox.insert('end', ftext)
                self.obox.see('end')
            else:
                break
                
    def data_processing_for_gui(self, data):
        procesed_str = ''
        for c in data:
            if c == '\x08':
                self.obox.delete("1.0", 'end')
            else:
                procesed_str = procesed_str + c

        return procesed_str

def send_task(telnet_inst, task):
    telnet_inst.write(b"\r\n" + task.encode('ascii') + b"\r\n")
    time.sleep(0.1)

def send_taska(telnet_inst, task, vendor = 'default', sleep_time = 0.1):
    debug_log('task: ' + task)
    debug_log('vendor: ' + vendor)
    if vendor == vd.Switch.RAISECOM.name:
        telnet_inst.write(task.encode('ascii') + b"\r")
    elif vendor == vd.Switch.DLINK_3200.name or vendor == vd.Switch.DLINK_3526.name:
        telnet_inst.write(b"\r\n" + task.encode('ascii') + b"\r\n")
        telnet_inst.write(b"\r\n" + "q".encode('ascii') + b"\r\n")
    elif vendor == 'default':
        telnet_inst.write(b"\r\n" + task.encode('ascii') + b"\n")
    time.sleep(sleep_time)
    #tmp_answer =  telnet_inst.read_very_eager().decode()
    #answer = tmp_answer

    return 1

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