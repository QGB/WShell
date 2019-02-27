net user administrator /active:yes


REM 电脑没有设置管理员密码的情况下无法进行远程桌面登录怎么办
REM 2、按Win+R打开运行，输入gpedit.msc并回车打开组策略编辑器;

REM 3、依次展开计算机配置——Windows设置——安全设置——本地策略——安全选项，并在右侧找到“帐户：使用空密码的本地帐户只允许进行控制台登录”，并将其设置“已停用”即可。

@rem 最后一行rem不会显示  ，为什么？