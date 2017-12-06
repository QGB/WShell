@echo off
: set PATH=G:\Python27\;G:\QGB\babun\cygwin\home\qgb\wshell
::test 


@for %%i in (python.exe) do @set py=%%~$PATH:i

@for %%i in ( %py%) do @set py=%%~dpi



@for /f "delims=" %%i in ('qpsu.bat "clipboard=f" "escape=t" "c=t"') do @set qp=%%i

: @echo %qp%
: if not x%py:conda=%==x%py% echo It contains conda
::if not contains conda  
if x%py:conda=%==x%py% set py=python %py%

%py%Scripts\ipython.exe --no-banner  --autocall=2  "--InteractiveShellApp.exec_lines=['%qp%']" %*

: --no-confirm-exit 