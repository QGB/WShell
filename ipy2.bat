@echo off
call %~dp0setqp.bat
%~dp0ipython2 %ipyArgs% %*