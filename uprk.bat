if not defined wspath (set wspath=G:\QGB\babun\cygwin\home\qgb\wshell\)
if "%*"=="" (for /f "delims=" %%i in ('%wspath%datetime.bat') do set commit_msg=%%i ) else (set commit_msg=%*)
for %%a in ("%cd%") do set repo=%%~nxa

git add -A

git config --local user.email 191176932@qq.com
git config --local user.name hnrunke

git config --global core.filemode false
git config --global credential.helper store

git commit -m "%commit_msg%"

call %QGB%rk.bat

git push origin master 