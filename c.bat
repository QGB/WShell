@if "%1"=="" (goto cl)

@python %~dp0py/cd.py %*

@goto end

:cl
@cls


:end
