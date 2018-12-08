@echo off
if defined QGB (goto end)

set path=%path%
set path=C:\Cygwin\bin;%path%
set path=C:\Program Files\Git\usr\bin;%path%
: @set path=C:\Program Files\Git\bin;%path%
: @set path=C:\Program Files\Git\cmd;%path%
: @set path=C:\Program Files\Git\mingw32\bin;%path%
: @set path=C:\Python27;%path%
: @set path=C:\Python27\Scripts;%path%
set path=D:\Cygwin\bin;%path%
set path=D:\Program Files\CodeBlocks\MinGW\bin;%path%
set path=D:\Program Files\FreeTime\FormatFactory\FFModules;%path%
set path=D:\Program Files\Git\bin;%path%
set path=D:\Program Files\Git\cmd;%path%
set path=D:\Program Files\Git\mingw32\bin;%path%
set path=D:\Program Files\Git\usr\bin;%path%
set path=D:\Program Files\Java\jdk1.7.0_25\bin;%path%
set path=D:\Program Files\Java\jdk1.8.0_45\bin;%path%
set path=D:\Program Files\nodejs;%path%
set path=G:\Program Files\Git\usr\bin;%path%
set path=G:\Program Files\Git\cmd;%path%

set path=D:\Program Files\ExcelsiorJET\bin;%path%
: @set HOME=D:\Program Files\Git\
: @set JAVA_HOME=D:\Program Files\Java\jdk1.8.0_45\

set wsPath=%~dp0
for %%i in (%~dp0) do @set wsDriver=%%~di
set QGB=%wsDriver%\QGB\

set conda=%QGB%Anaconda2\
set conda3=%QGB%Anaconda3\
set path=%conda3%;%conda3%Scripts;%conda3%Library\bin;%path%
set path=%conda%;%conda%Scripts;%conda%Library\bin;%path%
set QPSU=%QGB%babun\cygwin\lib\python2.7\qgb\

set path=%APPDATA%\npm\;%path%
set path=%QGB%nodejs\;%path%


set path=%~dp0;%path%
set path=%~dp0exe;%path%

@REM if not defined MOBANOACL (start  /b  wSetx.bat)
@REM if not defined MOBANOACL (%~dp0exe/pos 77 -12)
@REM in mobaXterm window wrong

echo @"%~dpnx0" > %windir%\ws.cmd
 : pause
:end 
%~dp0clink/clink inject

