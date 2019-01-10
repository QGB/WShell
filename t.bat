@echo off
setlocal EnableDelayedExpansion
set mystring=%*

echo %mystring%

if !mystring:~0^,1!!mystring:~-1! equ "" (
   echo -^> String is quoted
) else (
   echo -^> String not quoted
   set newstring="%mystring%"
   echo New string: !newstring!
)
echo/








@REM ipython.exe --no-banner  --autocall=2 "--InteractiveShellApp.exec_lines=[ 'import sys;\'qgb.U\' in sys.modules or sys.path.append(\'G:/QGB/babun/cygwin/lib/python2.7/\');from qgb import *','NPP=npp=U.npp;py=U.py']"




@REM IF NOT DEFINED ipyArgs (set ipyArgs=--no-banner  --autocall=2 --InteractiveShellApp.exec_lines=["import sys;'qgb.U' in sys.modules or sys.path.append('G:/QGB/babun/cygwin/lib/python2.7/');from qgb import *",'NPP=npp=U.npp;py=U.py']

@REM @echo off

@REM set py=906bcd654654
@REM if not x%py:bcd=%==x%py% echo It contains bcd

@REM : echo @"%~dp0cyg.bat" > %windir%\ws.cmd
 
@REM : apk<nul

@REM @set p=python -c "import sys;print repr(sys.stdin.read(-1))"

@REM set p=python

@REM %P%
@REM )> bat.txt