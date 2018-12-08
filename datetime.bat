@echo off
for /F "delims=" %%i  in ('date /t') do (set sdate=%%i)
for /f "delims=" %%i in ('time /t') do (set stime=%%i)

set sdate=%sdate: =%

set datetime=%sdate%_%stime%

echo %datetime%