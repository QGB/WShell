@if "%1"=="" (goto help)

git init&@grepo %1&gqgb&gpull %1

@goto end

:help
@echo %0% repo

:end