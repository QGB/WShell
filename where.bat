@for %%i in (%*) do @if not "%%~$PATH:i"=="" (echo %%~$PATH:i) else echo %%i
