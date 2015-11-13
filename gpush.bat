@if "%1%"=="" (goto help)
@if "%2%"=="" (goto help)


git add -A
git commit -m %2%
git push %1%

:help
@echo %0% repo commitMsg