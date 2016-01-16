@echo off

set c=%1%
if %c%=="" goto end

set c1=%c:~0,1%
set c2=%c:~-3%

:echo c2%c2%
rem if %c2%==".py" goto py

if %c1%==- goto cmd

goto py

:py
python -m profile -s time %1%.py
goto end

:cmd
title Python Cmd
python %1%
goto end

:end
