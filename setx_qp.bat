set ws=%~dp0
for %%i in (%~dp0) do @set wsDriver=%%~di
set QGB=%wsDriver%\QGB\
set QPSU=%wsDriver%/QGB/babun/cygwin/bin/
@rem test
set QPSU=%wsDriver%/test/


set qp = import sys;\'qgb.U\' in sys.modules or sys.path.append(\'%QPSU%\');from qgb import *;C=c=U.clear

setx qp "import sys;\'qgb.U\' in sys.modules or sys.path.append(\'%QPSU%\');from qgb import *;C=c=U.clear"

set QPSU=%QPSU%qgb/
setx QPSU %QPSU%

set qp=
set ipyArgs=
