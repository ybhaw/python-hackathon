from easygui import *
import os
from sys import *
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

dc()