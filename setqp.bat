@echo off

IF NOT DEFINED qp (goto setqp)
IF NOT DEFINED pyPath (goto setqp)

set ipyargs=
IF NOT DEFINED ipyArgs (set ipyArgs=--no-banner  --autocall=2 "--InteractiveShellApp.exec_lines=['%qp%','NPP=npp=U.npp;py=U.py;r=R=U.r','sys.path.pop()']" )

goto end
::warnning not check pyPath


:setqp
set wsPath=%~dp0
for %%i in (%~dp0) do @set wsDriver=%%~di
set QGB=%wsDriver%\QGB\
IF NOT DEFINED py3path (set py3path=%QGB%Anaconda3\)


for %%i in (python.exe) do @set py=%%~$PATH:i

for %%i in ( %py%) do @set pyPath=%%~dpi




for /f "delims=" %%i in ('qpsu.bat "clipboard=f" "escape=t" "c=t"') do @set qp=%%i


setx qp "%qp%"
setx pyPath %pyPath%\


:end

