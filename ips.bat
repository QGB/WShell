@echo off
setlocal enabledelayedexpansion

for /f "tokens=1" %%a in ('net view') do (
  set comp=%%a & set comp=!comp:\\=!
  for /f "tokens=2 delims=[]" %%b in (
    'ping -4 !comp!'
  ) do (Echo !comp! - %%b)
)