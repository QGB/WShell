@python %~dp0py/npp.py %*
@goto end

@set path=%path%
@set path=C:\Program Files\Notepad++;%path%

@if "%1"=="" (goto end)

notepad++.exe %1
@goto end



:end
