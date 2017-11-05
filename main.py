#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scapy.all import *
import json
import requests
import logging

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.DEBUG)
setting = json.load(open("./settings.json", "r"))
url = "http://{server_host}:{server_port}/api/stop/".format(**setting)

def main():
    logging.info("waker-dash-button is up.")
    sniff(prn=arp_detect, filter="arp", store=0)

def arp_detect(packet):
    if packet[ARP].hwsrc == setting["mac_address"]:
        logging.info("Button is pushed.")
        requests.get(url)

if __name__=='__main__':
    main()
