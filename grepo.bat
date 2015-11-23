@if "%1"=="" (goto help)

git remote add %1 git@github.com:QGB/%1.git
@goto end

:help
@echo %0% repo

:end
