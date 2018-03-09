'''

Simple Subnet Calculator!
Gives you number of hosts avaliable in the subnet along with other network node addresses

Author: Swapnasheel Sonkamble
Usage: python Subnet_calculator.py 

Can add:
    - Argparse

'''

import random
import sys

def Main():

    try:
        print "\n"
         
        while True:
            ip_add = raw_input("Enter an IP address: ").split('.')

            '''
            Check for a valid IP address
            Make sure the IP address has:
                1. 4 Octets
                2. Maximum value of 255 in each octet
                3. Check for Link local IP address
                4. Not loopback or belonging to class E
            '''

            if ( len(ip_add) == 4) and (1 <= int(ip_add[0]) <= 255) and int(ip_add[0])!=0 and (int(ip_add[0])!=169) or int(ip_add[1])!=254 and int(ip_add[0]) != 224 and (1 <= int(ip_add) <= 255) and (1 <= int(ip_add[2]) <= 255) and (1 <= int(ip_add[3]) <= 255):
                break

            else:
                print "Ip address invalid!!! Please retry!!"
                continue

        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        while True:
            subnet_mask = raw_input("Enter the subnet mask: ").split('.')

            # Subnet mask checking as per above checks

            if ( len(subnet_mask) == 4 and int(subnet_mask[0]) == 255 and (int(subnet_mask[1]) in masks) and (int(subnet_mask[2]) in masks) and (int(subnet_mask[3]) in masks) and int(subnet_mask[0]) >= int(subnet_mask[1]) >= int(subnet_mask[2]) >= int(subnet_mask[3])):
                break

            else:
                print "Subnet mask error!! Please retry!!"
                continue

        
        # Convert subnet mask in binary
        mask_octet_padded = []
        mask_octet_decimal = subnet_mask

        #print mask_octet_decimal

        for octet_index in range(0, len(mask_octet_decimal)):

            #print bin(int(mask_octet_decimal[octet_index]))
            binary_octet = bin(int(mask_octet_decimal[octet_index])).split("b")[1]
            #print binary_octet

            # Check for length and add padded 0's

            if len(binary_octet) == 8:
                mask_octet_padded.append(binary_octet)

            elif len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                mask_octet_padded.append(binary_octet_padded)

        decimal_mask = "".join(mask_octet_padded)
        print decimal_mask  # this should print something like 255.255.255.0 -> 11111111111111111111111100000000

        # Lets count the number of 0's and 1's in the decimal mask

        number_of_zero = decimal_mask.count("0")
        number_of_ones = 32 - number_of_zero

        # To calculate the number of hosts in the network ->>> host = (2^n - 2)
        number_of_hosts = abs(2 ** number_of_zero - 2)

        #print number_of_zero
        #print number_of_ones
        #print number_of_hosts

        ## Calculate the wildcard mask













        

    except:
        print "Main Error!!"


if __name__ == '__main__':
    Main()


