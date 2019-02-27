@echo off
if not defined QGB (%QGB%Anaconda2\python.exe %*) else (goto qgb)
goto end

:qgb
%QGB%Anaconda2\python.exe %*

:end