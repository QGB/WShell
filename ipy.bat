@echo off
call setqp.bat

if "%1%"=="2" (goto ipy2)
if "%1%"=="3" (goto ipy3) else (goto ipy2)

if "%*"=="" (goto ipy2)

goto end
:ipy2
::if not contains conda  #todo  多次调用 可能会重复设置
REM if x%pyPath:conda=%==x%pyPath% (set pyPath=python %pyPath%)

%pyPath%Scripts\ipython.exe %ipyArgs%
goto end


:ipy3
ipython3 %ipyArgs%
goto end
:: ipy 2 3 有重复参数，为了可读性，放弃DRY吧。。。

: --no-confirm-exit 

: set PATH=G:\Python27\;%QGB%babun\cygwin\home\qgb\wshell
::test 

: @echo %qp%
: if not x%py:conda=%==x%py% echo It contains conda
: --no-confirm-exit 

:end