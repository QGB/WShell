if "%gitUser%"=="" (set gitUser=QGB)
if "%gitMail%"=="" (set gitMail=qgbcs1@gmail.com)
@rem 更换用户名 需要在 【凭据管理器】》【Windows】 中删除原来的
for %%a in ("%cd%") do set gitRepo=%%~nxa

git pull cq master
@rem 如果没有国内git加速，需要改为 origin



if not defined wspath (set wsPath=%~dp0)
for %%i in (%~dp0) do @set wsDriver=%%~di
set QGB=%wsDriver%\QGB\

if "%*"=="" (for /f "delims=" %%i in ('%wspath%datetime.bat') do set commit_msg=%%i ) else (set commit_msg=%*)
if "%commit_msg%"=="" (set commit_msg="default up")


git config --global user.email %gitMail%
git config --global user.name %gitUser%


git config --global http.sslverify "false"
git config --global core.filemode false
git config --global credential.helper store

git remote add q https://github.com/%gitUser%/%gitRepo%
git remote add cq https://coding.net/u/%gitUser%/p/%gitRepo%/git/
git add -A
git commit -m "%commit_msg%"
git push cq master 
git push q master 