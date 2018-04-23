@if "%1%"=="" (goto help)
@if "%2%"=="" (goto outdf)
@goto out

:outdf
@set st=png
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
set path=D:\Program Files\Graphviz2.38\bin;%path%
@echo %0% XX[.dot] [OutType(jpg,ps,etc)] 
@goto end

:end