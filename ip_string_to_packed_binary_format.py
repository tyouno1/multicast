import binascii
import socket
import struct
import sys

string_address = sys.argv[1]
packed = socket.inet_pton(socket.AF_INET, string_address)

print 'Original:', string_address
print 'Packed  :', binascii.hexlify(packed)
print 'Unpacked:', socket.inet_ntop(socket.AF_INET, packed)
