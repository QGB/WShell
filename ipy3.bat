@echo off

call setqp.bat


:ipy3

ipython3 %ipyArgs% %*

: --no-confirm-exit 