import os
import subprocess

directlist = open('direct').read().splitlines()
direct_no_dup = open('direct_no_dup', 'w')

domains = list(set(directlist))
domains.sort()

for domain in domains:
    direct_no_dup.write(domain + '\n')
    print domain

direct_no_dup.close()
