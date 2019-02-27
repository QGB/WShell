echo @"%QGB%babun\cygwin\home\qgb\wshell\wshell.bat" > %windir%\ws.cmd
echo @rem  > %windir%\n2.cmd
echo net use g: /delete > %windir%\n2.cmd
echo net use g: \\192.168.1.222\g 0 /user:administrator >> %windir%\n2.cmd

copy /Y %~dp0file\python27.dll  %windir%
