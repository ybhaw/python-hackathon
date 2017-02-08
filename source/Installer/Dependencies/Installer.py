from easygui import *
import sys
import os
import webbrowser

#This segment is for downloadables................................................................

def dc():
	if ccbox("Confirm you want to install DC++","DC installer"):
		os.system("start dc.exe")
		k="""Do you want to create a large file for upload On Dc?
Note that most IITB-Hubs require you to have atleast 25gb of shared file"""
		if ccbox(k, title=' ', choices=('Y[e]s', 'C[a]ncel'), image=None, default_choice='Yes', cancel_choice='Cancel'):
			a=integerbox("Enter the size of file you want to create In GB","Spam File Maker","25",1,100)
			a=str(a*1024**3)
			b="md c:\IITBS\DC\Upload"
			os.system(b)
			c="del c:\IITBS\DC\Upload\dc_spam"
			os.system(c)
			a='fsutil file createnew \"c:\IITBS\DC\Upload\dc_spam\" '+a
			os.system(a)
		return True
	else:
		return False
		
def extra_Package():
	webbrowser.open_new("ninite.com")

def downloads():
	l=["DC++","Extra Packages"];
	result=multchoicebox("Select the features you want to install", "Features Window", l)
	try:
		if "DC++" in result : dc();
	except:
		print "hello"
	try:
		if "Extra Packages" in result : extra_Package()
	except:
		print "Hello"

#This segment is for features that is to be included..............................................
def LAN_IP_Configure():
	if ccbox("Do you want to continue?","IP-Configure"):
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
		else : 
			hostel='16'
			l=30
		m=map(str,range(1,11))
		floor=choicebox("Select on which floor you live","IP-Configure",m);
		floor=str(int(floor)+l)
		k=integerbox("Enter Your RollNumber", "IP-Configure",16,160000000,180000000)
		k=str(k%100);
		ip='10.'+hostel+'.'+floor+'.'+k
		sn='255.255.255.0'
		dg='10.'+hostel+'.'+floor+'.250'
		command="netsh interface ip set address name=\"Ethernet\" static "+ip+" "+sn+" "+dg
		os.system(command)
		dn='10.200.1.11'
		t="netsh interface ip set dns name=\"Ethernet\" static "+dn
		os.system(t)
		return True
	else :
		return False
		
def INTERNET_IITB_AutoLogin():
	k="""DAP-LOGIN auto logs you into internet.iitb.ac.in whenever you sign-in into the current user account.
	
	Do you want to continue?"""
	if ccbox(k,"DAP-Login"):
		os.system("start setup1.exe")
		kaa=enterbox("Enter your LDAP-ID","internet.iitb-AutoLogin")
		laa=passwordbox("Enter your LDAP-Password","internet.iitb-AutoLogin")
		cmd="start C:/IITBS/DAPL/DAP-Login.exe "+kaa+" "+laa
		os.system(cmd)
		os.system("start C:/IITBS/DAPL/Login-bot.exe")
		return True
	else : return False

def IITB_Wireless_Config():
	os.system("call IITBW.exe")
	
def features():
	l=["LAN-IP-Configure","INTERNET.IITB-AutoLogin","IITBWireless-Config"]
	result=multchoicebox("Select the features you want to install", "Features Window", l)
	try:
		if "LAN-IP-Configure" in result : LAN_IP_Configure();
	except:
		print "hello"
	try:
		if "INTERNET.IITB-AutoLogin" in result : INTERNET_IITB_AutoLogin()
	except:
		print "hello"
	try:
		if "IITBWireless-Config" in result : IITB_Wireless_Config();
	except:
		print "hello"
	downloads()

#MAIN SECTION____________________________________
	
def main1():
	apple="""IITB Soft-Stall

	One package for downloading, installing and configuring all the iitb-must have softwares.

	Press 'proceed' to proceed to the features directory
	"""

	k=msgbox(apple,'Soft-Stall',"proceed")
	if (k=="proceed") : features();
	msgbox("Thanks for installing the software","Soft-Stall","Close")

zz=os.system('cls')
print "program by Vaibhaw & Pratyush"
main1()
