: @echo off
set wsPath=%~dp0
for %%i in (%~dp0) do @set wsDriver=%%~di
set QGB=%wsDriver%\QGB\


@if not defined wsDriver   (setx wsDriver %wsDriver%)
@if not defined QGB   (setx QGB %QGB%)
REM @if not defined QGB   (call %~dp0wshell.bat)
@if not defined JAVA_HOME (setx JAVA_HOME F:\Java\jdk1.7.0_25)
@if not defined py3path   (setx py3path %QGB%Anaconda3\)
@if not defined wsPath    (setx wsPath %~dp0)
@if not defined gst    (goto gst)

@goto end

:gst
@for /f "delims=" %%i in ('python %~dp0py/cd.py %*') do @set "gst=%%i"
@setx gst "%gst%"
@goto end

:end
@echo %0
