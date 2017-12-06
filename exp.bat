@if "%1"=="" (goto curr)

@start "" explorer %1
@goto end

:curr
@start "" explorer .

:end