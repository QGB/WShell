set ws=%~dp0
for %%i in (%~dp0) do @set wsDriver=%%~di
set QGB=%wsDriver%\QGB\
set QPSU=%wsDriver%/QGB/babun/cygwin/bin/
set qp=import sys;\'qgb.U\' in sys.modules or sys.path.append(\'%wsDriver%/QGB/babun/cygwin/bin/\');from qgb import *;C=c=U.clear

setx QPSU %wsDriver%/QGB/babun/cygwin/bin/
setx qp "import sys;\'qgb.U\' in sys.modules or sys.path.append(\'%QPSU%\');from qgb import *;C=c=U.clear" 
