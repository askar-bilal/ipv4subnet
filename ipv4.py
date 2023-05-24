from asyncio.windows_events import NULL
import re

def ipv4Check(ipv4):
    #pattern: xxx.xxx.xxx.xxx/xx
    pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}$")
    match = re.match(pattern, ipv4)
    if(match):
        result = True
        ipAddress = ipv4.split('/')[0]
        ipPrefix = ipv4.split('/')[1]
        if not(int(ipPrefix) >=0 and int(ipPrefix) <= 32):
            result = False
        octets=ipAddress.split(".")
        for i in range(0, len(octets)):
            if not(int(octets[i])>=0 and int(octets[i])<=255):
                result = False
        return result
    else:
        return False

def ipv4pref(ipv4):
    ipv4address = "Ipv4 address is wrong"
    if ipv4Check(ipv4):
        ipv4address = ipv4.split('/')[1]
    return ipv4address

def ipAddress(ipv4):
    ipv4address = "Ipv4 address is wrong"
    if ipv4Check(ipv4):
        ipv4address = ipv4.split('/')[0]
    return ipv4address

def ipv4AddressToBin(ipv4):
    binary= "Ipv4 address is wrong"
    if ipv4Check(ipv4):
        binary = '{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(*map(int, ipAddress(ipv4).split('.')))
    return binary

def ipv4Subnet(ipv4):
    subnet="Ipv4 address is wrong"
    if ipv4Check(ipv4):
        for oct in ipv4SubnetToBin(ipv4).split('.'):
            if subnet== "Ipv4 address is wrong":
                subnet=int(oct,2)
            else:
                subnet=f'{subnet}.{int(oct,2)}'
    return subnet

def ipv4SubnetToBin(ipv4):
    subnet="Ipv4 address is wrong"
    if ipv4Check(ipv4):
        pref = int(ipv4.split('/')[1])
        subnet=("1"*pref+"0"*(32-pref))
        subnet = '.'.join(subnet[i:i+8] for i in range(0, len(subnet), 8))
    return subnet



def ipv4Wildcast(ipv4):
    subnet="Ipv4 address is wrong"
    if ipv4Check(ipv4):
        for oct in ipv4SubnetToBin(ipv4).split('.'):
            oct=~int(oct,2) & 255
            if subnet== "Ipv4 address is wrong":
                subnet=oct
            else:
                subnet=f'{subnet}.{oct}'
    return subnet

def ipv4WildcastToBin(ipv4):
    subnet="Ipv4 address is wrong"
    if ipv4Check(ipv4):
        for oct in ipv4SubnetToBin(ipv4).split('.'):
            oct=~int(oct,2) & 255
            if subnet== "Ipv4 address is wrong":
                subnet=oct
            else:
                subnet=f'{subnet}.{oct}'
    return subnet

def ipv4Hosts(ipv4):
    hosts="Ipv4 address is wrong"
    if ipv4Check(ipv4):
        pref = int(ipv4.split('/')[1])
        hosts=2**(32-pref)
    return hosts

#print(ip2bin('192.168.2.1/24'))
#print(ip2subnet('192.168.2.1/24'))
#print("----")
#print("Enter the IPv4 address with the prefix: 192.168.2.1/24")
#ipv4 = input("Enter the IPv4 address with the prefix:")
#aaa=ipv4Check(ipv4)
#print(aaa)

ipv4="192.168.1.1/24"
print(20*'-')
print(f'Kontrol: {ipv4Check(ipv4)}')
print(20*'-')
print(f'Adres: {ipAddress(ipv4)}')
print(f'CIDR: {ipv4pref(ipv4)}')
print(f'Binary Adres: {ipv4AddressToBin(ipv4)}')
print(20*'-')
print(f'Subnet: {ipv4Subnet(ipv4)}')
print(f'Binary Subnet: {ipv4SubnetToBin(ipv4)}')
print(20*'-')
print(f'Hosts: {ipv4Hosts(ipv4)}')
print(20*'-')
print(f'Wildcast: {ipv4Wildcast(ipv4)}')
print(f'Binary Wildcast: {ipv4WildcastToBin(ipv4)}')