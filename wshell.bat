@set path=%path%
@set path=C:\Cygwin\bin;%path%
: @set path=C:\Program Files\Git\bin;%path%
: @set path=C:\Program Files\Git\cmd;%path%
: @set path=C:\Program Files\Git\mingw32\bin;%path%
: @set path=C:\Python27;%path%
: @set path=C:\Python27\Scripts;%path%
@set path=D:\Cygwin\bin;%path%
@set path=D:\Program Files\CodeBlocks\MinGW\bin;%path%
@set path=D:\Program Files\FreeTime\FormatFactory\FFModules;%path%
@set path=D:\Program Files\Git\bin;%path%
@set path=D:\Program Files\Git\cmd;%path%
@set path=D:\Program Files\Git\mingw32\bin;%path%
@set path=D:\Program Files\Git\usr\bin;%path%
@set path=D:\Program Files\Java\jdk1.7.0_25\bin;%path%
@set path=D:\Program Files\Java\jdk1.8.0_45\bin;%path%
@set path=D:\Program Files\nodejs;%path%


@set path=%~dp0;%path%
@set path=%~dp0exe;%path%

@set path=D:\Program Files\ExcelsiorJET\bin;%path%

: @set HOME=D:\Program Files\Git\

@set JAVA_HOME=D:\Program Files\Java\jdk1.8.0_45\

@set wsPath=%~dp0
@for %%i in (%~dp0) do @set wsDriver=%%~di
@set QGB=%wsDriver%\QGB\

@set conda=%QGB%Anaconda2\
@set path=%conda%;%conda%Scripts;%path%

@set QPSU=%QGB%babun\cygwin\lib\python2.7\qgb\


@echo @"%~dpnx0" > %windir%\ws.cmd
: pause
@%~dp0exe/pos 77 -12
@%~dp0clink/clink inject

