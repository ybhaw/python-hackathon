# -*- coding: utf-8 -*-
import sys
import os
ip=sys.argv[1]
sn=sys.argv[2]
dg=sys.argv[3]
command="netsh interface ip set address name=\"Ethernet\" static "+ip+" "+sn+" "+dg
os.system(command)
dn=sys.argv[4]
t="netsh interface ip set dns name=\"Ethernet\" static "+dn
os.system(t)
