@echo off
if not defined QGB (G:\QGB\Anaconda3\python.exe %*) else (goto qgb)
goto end

:qgb
%QGB%Anaconda3\python.exe %*

:end