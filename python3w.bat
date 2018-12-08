@echo off
if not defined QGB (G:\QGB\Anaconda3\pythonw.exe %*) else (goto qgb)
goto end

:qgb
%QGB%Anaconda3\pythonw.exe %*

:end