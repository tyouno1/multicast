#! /usr/bin/python

import re
import sys
import socket

def convert_multicast_ip_to_mac(ip_address):
    """Convert the Multicast IP to it's equivalent Multicast MAC.
    Source info: https://technet.microsoft.com/en-us/library/cc957928.aspx
    """
    # Convert the IP String to a bit sequence string
    try:
        ip_binary = socket.inet_pton(socket.AF_INET, ip_address)
        ip_bit_string = ''.join(['{0:08b}'.format(ord(x)) for x in ip_binary])
    except socket.error:
        raise RuntimeError('Invalid IP Address to convert.')

    # The low order 23 bits of the IP multicast address are mapped directly to the low order
    # 23 bits in the MAC-layer multicast address
    lower_order_23 = ip_bit_string[-23:]

    # The high order 25 bits of the 48-bit MAC address are fixed
    high_order_25 = '0000000100000000010111100'

    mac_bit_string = high_order_25 + lower_order_23

    # Convert the bit string to the Typical MAC Address String
    final_string = '{0:012X}'.format(int(mac_bit_string, 2))
    mac_string = ':'.join(s.encode('hex') for s in final_string.decode('hex'))
    return mac_string.upper()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Try the function with multiple IPs
        first = '225'
        for i in range(1, 4048, 8):
            fourth = (i % 255)
            third = ((i / 255) % 255)
            second = 20+(i / 65025)
            ip = '{0}.{1}.{2}.{3}'.format(first, second, third, fourth)
            print ip, '-', convert_multicast_ip_to_mac(ip)
    else:
        try:
            while True:
                user_input = raw_input('Enter the IP Address to Convert (^C to quit): ')
                try:
                    print 'Result:', convert_multicast_ip_to_mac(user_input)
                    #convert_multicast_ip_to_mac(user_input)
                except RuntimeError as e:
                    print str(e)

        except KeyboardInterrupt:
            print '\nCiao...'
