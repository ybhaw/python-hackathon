@echo off

rem Taking Input
rem .............................................................

set ldap=%1%

set passwo=%2%

rem deleting previous files
rem ..............................................................

if exist C:\IITBS\DAPL\config.vbs del /q C:\IITBS\DAPL\config.vbs
if exist C:\IITBS\DAPL\config.dll del /q C:\IITBS\DAPL\config.dll

rem Making config files
rem ..............................................................

echo Set IE = CreateObject("InternetExplorer.Application") >C:\IITBS\DAPL\config.vbs
echo IE.navigate "http://internet.iitb.ac.in" >>C:\IITBS\DAPL\config.vbs
echo IE.Visible = False >>C:\IITBS\DAPL\config.vbs
echo On Error Resume Next >>C:\IITBS\DAPL\config.vbs
echo While IE.Busy >>C:\IITBS\DAPL\config.vbs
echo     WScript.Sleep 50 >>C:\IITBS\DAPL\config.vbs
echo Wend >>C:\IITBS\DAPL\config.vbs
echo If (IE.document.all.name) is Nothing Then >>C:\IITBS\DAPL\config.vbs
echo 	Set ipf = IE.document.all.uname >>C:\IITBS\DAPL\config.vbs
echo 	ipf.Value = "%ldap%"  >>C:\IITBS\DAPL\config.vbs
echo	Set ipf = IE.document.all.passwd >>C:\IITBS\DAPL\config.vbs
echo 	ipf.Value = "%passwo%" >>C:\IITBS\DAPL\config.vbs
echo 	Set ipf = IE.document.all.button >>C:\IITBS\DAPL\config.vbs
echo 	ipf.Click  >>C:\IITBS\DAPL\config.vbs
echo Else >>C:\IITBS\DAPL\config.vbs
echo 	msg = "Already Logged In" >>C:\IITBS\DAPL\config.vbs
echo End If >>C:\IITBS\DAPL\config.vbs
echo IE.Quit >>C:\IITBS\DAPL\config.vbs

rem Encrypting
rem ...............................................................

%extd% /lzma "C:\IITBS\DAPL\config.vbs" "C:\IITBS\DAPL\config.dll"
del /q "C:\IITBS\DAPL\config.vbs"
exit

