echo @"%~dp0wshell.bat" > %windir%\ws.cmd
echo net use g: \\tsclient\G > %windir%\n.cmd

copy /Y %~dp0file\python27.dll  %windir%
