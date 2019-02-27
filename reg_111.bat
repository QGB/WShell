echo @"%QGB%babun\cygwin\home\qgb\wshell\wshell.bat" > %windir%\ws.cmd
echo @rem  > %windir%\n.cmd
@REM echo net use g: /delete > %windir%\n.cmd
echo net use g: \\192.168.1.111\g 0 /user:administrator >> %windir%\n.cmd

copy /Y %~dp0file\python27.dll  %windir%
