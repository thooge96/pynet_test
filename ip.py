#!/usr/bin/env python
from __future__ import print_function

try:
    ip_addr=raw_input("IP:")
except NameError:
    ip_addr=input("IP:")

octets=ip_addr.split(".")

print ("\n{:^20}{:^20}{:^20}{:^20}\n".format(*octets))



