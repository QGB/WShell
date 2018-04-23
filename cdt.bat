: @d:





@for /f "delims=" %%i in ('python %~dp0py/cd.py %*') do @set cdPath=%%i

: @echo "%cdpath%"

@%cdpath%


: @%wsdriver%
: @cd \test\%1
