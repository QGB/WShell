@if "%1"=="" (goto curr)

@explorer %1
@goto end

:curr
@explorer .

:end