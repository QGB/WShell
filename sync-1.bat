for %%i in (%~dp0) do @set wsDriver=%%~di
%wsDriver%\QGB\software\FastCopy\FastCopy.exe /cmd=update \\192.168.1.%1\g\QGB\%2 /to=%wsDriver%\QGB\%2