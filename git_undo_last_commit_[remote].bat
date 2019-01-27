git pull origin  master
@echo #####  真的要撤销远程的提交吗？ctrl+c 取消
pause
git reset --hard HEAD~1
git push -f