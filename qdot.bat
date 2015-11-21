@if "%1%"=="" (goto help)
@if "%2%"=="" (goto outdf)
@goto out

:outdf
@set st=jpg
@goto setf

:out
@set st=%2
@goto setf

:setf
@set t=%1
@set t=%t:~-4%
@if "%t%"==".dot" (goto exten)
@if "%t%"==".DOT" (goto exten)
@set fn=%1.dot
@goto main

:exten
@set fn=%1
@goto main


:main
dot -T%st% %fn% -o %fn%.%st%
start "" "%fn%.%st%"
@goto end

:help
@echo %0% XX[.dot] OutType(jpg,ps,etc) 
@goto end

:end