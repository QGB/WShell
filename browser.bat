@echo off
setlocal EnableDelayedExpansion
set mystring=%*

REM echo %mystring%

if !mystring:~0^,1!!mystring:~-1! equ "" (
   echo -^> String is quoted
   %USERPROFILE%\AppData\Local\Yandex\YandexBrowser\Application\browser.exe %mystring%
) else (
   echo -^> String not quoted
   %USERPROFILE%\AppData\Local\Yandex\YandexBrowser\Application\browser.exe "%mystring%"
)
echo/




@REM set variable=%*
@REM IF "%variable:~0,1%"==""" (set f=%variable%) else (set f="%variable%")
REM %USERPROFILE%\AppData\Local\Yandex\YandexBrowser\Application\browser.exe %*
REM pause

@REM 使用everything打开时，会自动加上 ""


@REM C:\Users\Administrator\AppData\Local\Yandex\YandexBrowser\Application\browser.exe ""C:\QGB\Document\三维空间子群网的推导 .pdf""

