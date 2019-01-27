echo @"G:\QGB\babun\cygwin\home\qgb\wshell\wshell.bat" > %windir%\ws.cmd
echo net use g: /delete > %windir%\n.cmd
echo net use g: \\qgb\g 0 /user:administrator >> %windir%\n.cmd

copy /Y %~dp0file\python27.dll  %windir%
