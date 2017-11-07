@for %%i in (python.exe) do @set py=%%~$PATH:i

@for %%i in ( %py%) do @set py=%%~dpi


: if "%1"==""


@for /f "delims=" %%i in ('qpsu.bat "clipboard=f" "escape=t" "c=t"') do @set qp=%%i

: @echo %qp%
@python %py%Scripts\ipython.exe --no-banner  --autocall=2  "--InteractiveShellApp.exec_lines=['%qp%']"

