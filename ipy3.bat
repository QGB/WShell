REM @echo off

call %~dp0setqp.bat


:ipy3

%~dp0ipython3 %ipyArgs% %*

: --no-confirm-exit 