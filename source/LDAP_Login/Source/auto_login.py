import easygui
import sys
import os

multchoice("a","a",['1','2'])

def LAN_IP_Configure():
	l=["hostel 15A","hostel 15B","hostel 15C","hostel 16A","hostel 16B","hostel 16C"]
	m=map(str,range(1,11))
	hostel=choicebox("Select in which hostel you live","IP-Configure",l);
	if ("hostel 15A" in hostel) : 
		hostel='15'
		l=10
	elif ("hostel 15B" in hostel) : 
		hostel='15'
		l=20
	elif ("hostel 15C" in hostel) : 
		hostel='15'
		l=30	
	elif ("hostel 16A" in hostel) : 
		hostel='16'
		l=10
	elif ("hostel 16B" in hostel) : 
		hostel='16'
		l=20
	elif ("hostel 16C" in hostel) : 
		hostel='16'
		l=30
	m=map(str,range(1,11))
	
	floor=choicebox("Select on which floor you live","IP-Configure",m);
	
	ip=sys.argv[1]
	
	sn=sys.argv[2]
	dg=sys.argv[3]
	command="netsh interface ip set address name=\"Ethernet\" static "+ip+" "+sn+" "+dg
	os.system(command)
	dn=sys.argv[4]
	t="netsh interface ip set dns name=\"Ethernet\" static "+dn
	os.system(t)


def features():
	l=["LAN-IP-Configure","IITB-Wireless-AutoLogin"]
	result=multchoicebox("Select the features you want to install", "Features Window", l)
	if "LAN-IP-Configure" in a : LAN_IP_Configure();

def main1():
	apple="""IITB Soft-Stall

	One package for downloading, installing and configuring all the iitb-must have softwares.

	Press 'proceed' to proceed to the features directory
	"""

	k=msgbox(apple,'Soft-Stall',"proceed")
	if (k=="proceed") : features();
