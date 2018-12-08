@if "%1"=="" (goto help)
dj makemigrations %*
dj migrate


:help
@echo off
echo %0 app_name