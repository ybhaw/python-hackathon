@echo off
cd %~dp0
md "C:\IITBS\DAPL"
copy ldap_login.exe "C:\IITBS\DAPL\dap_login.exe"
copy login_bot.exe "C:\IITBS\DAPL\login_bot.exe"
reg import regis.reg
exit