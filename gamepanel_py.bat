REM 用管理员身份运行 
REM bat 脚本默认32位？文件操作重定向到 C:\Windows\SysWOW64

del /f C:\WINDOWS\system32\GamePanel.exe

mv %QGB%py\py.exe C:\WINDOWS\system32\GamePanel.exe