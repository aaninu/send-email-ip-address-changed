import urllib.request
import requests
from requests import get
import os

def get_ip_01():
    return [urllib.request.urlopen('https://ident.me').read().decode('utf8'), 'https://ident.me']

def get_ip_02():
    return [get('https://api.ipify.org').text, 'https://api.ipify.org']

def get_ip_03():
    return [requests.get('https://checkip.amazonaws.com').text.strip(), 'https://checkip.amazonaws.com']

def get_ip_04():
    return [os.popen('curl -s ifconfig.me').readline(), 'https://ifconfig.me']

def get_ip():
    ip1 = get_ip_01()
    ip2 = get_ip_02()
    ip3 = get_ip_03()
    ip4 = get_ip_04()
    ipList = []
    ipList.append([ip1[0], ip1[1]])
    if (ip2[0] != ip1[0]):
        ipList.append([ip2[0], ip2[1]])
    if (ip3[0] != ip2[0] and ip3[0] != ip1[0]):
        ipList.append([ip3[0], ip3[1]])  
    if (ip4[0] != ip3[0] and ip4[0] != ip2[0] and ip4[0] != ip1[0]):
        ipList.append([ip4[0], ip4[1]])
    return ipList
