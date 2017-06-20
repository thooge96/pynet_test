from __future__ import print_function

name1="Tim"
name2="Barry"
name3="Ron"

try:
    in_name=raw_input("Enter a Name Version 2")
except NameError:
    in_name=input("Enter a Name Version 3")


print("{:>30}{:>30}{:>30}{:>30}".format(name1,name2,name3,in_name))



