@echo off
if not defined QGB (%QGB%Anaconda3\pythonw.exe %*) else (goto qgb)
goto end

:qgb
%QGB%Anaconda3\pythonw.exe %*

:end