# !/usr/bin/env python3

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP()
    print(arp_request.summary())
    # scapy.arping(ip)
    scapy.ls(scapy.ARP())



scan("192.168.43.1/24")
