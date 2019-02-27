import telnetlib as tlb
import time
import sys

import threading




        


print("Exiting main thread")


tl_obj = tlb.Telnet("172.17.51.51")

tl_obj.write("sam".encode('ascii') + b'\r')
time.sleep(0.1)
tl_obj.write("osinkii".encode('ascii') + b'\r')

time.sleep(0.1)
tl_obj.write("help".encode('ascii') + b'\r')

thr1 = AsyncHi(tl_obj)

thr1.start()



tl_obj.write("exit".encode('ascii') + b'\r')

tl_obj.close()