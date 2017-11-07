@python "E:\SourceCode\shell\py\_pyhelp.py" %*
@goto end
if "%1%"=="" (goto help)
if "%2%"=="" (goto setp)
set p=from %2 


goto main


:setp
set p=
mkdir d:\test\pyhelp
set f="d:\test\pyhelp\%1.html"
goto main

:main

python -c "%p%import %1;help(%1)" > %f%
goto end


:help
echo %0% obj [package]
goto end


:end