@if "%1"=="" (goto help)

git pull %1 master
@goto end

:help
@echo %0% repo

:end