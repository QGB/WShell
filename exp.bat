@if "%1"=="" (goto curr)

@start "" explorer %1
cd %1

@goto end

:curr
@start "" explorer .

:end
