@echo off
if not defined QGB (%QGB%Anaconda3\python.exe %*) else (goto qgb)
goto end

:qgb
%QGB%Anaconda3\python.exe %*

:end