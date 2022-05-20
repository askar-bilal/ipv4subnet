import ipaddress
import re

def ipv4Check(ipWithPrefix):
    #pattern: xxx.xxx.xxx.xxx/xx
    pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}$")
    match = re.match(pattern, ipWithPrefix)
    if(match):
        fields = ipWithPrefix.split("/")
        ipAddress = fields[0]
        ipPrefix = fields[1]
        pref=True
        oct=True
        if not (int(ipPrefix) >=0 and int(ipPrefix) <= 32):
            pref=False
        octets=ipAddress.split(".")
        for i in range(0, len(octets)):
            if not(int(octets[i])>=0 and int(octets[i])<=255):
                oct=False
        if(pref and oct):
            print("eslesti:"+ ipWithPrefix)
            print("Ipadress: "+ipAddress)
            print("IpPrefix: "+ipPrefix)
        else:
            if not (pref):
                print("Prefix must be between 0-32")
            if not (oct):
                print("Each Octet values must be between 0-255")
    else:
        print("IPv4 format problem for this input: "+ ipWithPrefix)
        print("IPv4 address should be like this(xxx.xxx.xxx.xxx/xx)")

print("Enter the IPv4 address with the prefix: 192.168.1/24")
ipv4 = input("Enter the IPv4 address with the prefix:")
ipv4Check(ipv4)


