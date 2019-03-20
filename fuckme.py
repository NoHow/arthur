import switch_proc as sp
import telnetlib as tl
import time
import tools as tls
import threading
import sys

bstr = b'\x08 \x08\x08 \x08\x08 \x08\x08 \x08\x08 \x08\x08 \x08\x08 \x08\x08 \x08\x08 \x08\x08 \x08\x08 \x08\x08 \x08\x08 \x08  23       '
print(bstr)
print(bstr.decode('ascii'))
print(repr(bstr.decode('ascii')))

for i in bstr.decode('ascii'):
    if repr(i) == '\x08':
        print(repr(i))
    else:
        print('no')