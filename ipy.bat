@echo off
call setqp.bat

if "%1%"=="2" (goto ipy2)
if "%1%"=="3" (goto ipy3) else (goto ipy2)

if "%*"=="" (goto ipy2)

goto end
:ipy2
::if not contains conda  #todo  ��ε��� ���ܻ��ظ�����
REM if x%pyPath:conda=%==x%pyPath% (set pyPath=python %pyPath%)

%pyPath%Scripts\ipython.exe %ipyArgs%
goto end


:ipy3
ipython3 %ipyArgs%
goto end
:: ipy 2 3 ���ظ�������Ϊ�˿ɶ��ԣ�����DRY�ɡ�����

: --no-confirm-exit 

: set PATH=G:\Python27\;%QGB%babun\cygwin\home\qgb\wshell
::test 

: @echo %qp%
: if not x%py:conda=%==x%py% echo It contains conda
: --no-confirm-exit 

:end