set wsPath=%~dp0
for %%i in (%~dp0) do @set wsDriver=%%~di
set QGB=%wsDriver%\QGB\

IF NOT DEFINED py3path (set py3path=%QGB%Anaconda3\)



%py3path%python.exe -c "import sys,os;sys.path.append('G:/QGB/babun/cygwin/bin');from qgb import *;U.cb.set(r''' site:zhihu.com ''')"

