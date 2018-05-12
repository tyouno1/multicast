import binascii
import socket

ip_32bit_list=[
'010000E0',
'FB0000E0',
'010000E0',
'FB0000E0',
'010000E0',
'FB0000E0',
'010000E0',
]

for sip in ip_32bit_list:
    ip_binary=binascii.unhexlify(sip)[::-1]
    print "Result:", sip ,'=>', socket.inet_ntop(socket.AF_INET,ip_binary)
