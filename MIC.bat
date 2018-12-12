REM https://zh.wikipedia.org/wiki/强制完整性控制
REM 为啥 只在 system32 下有效？  otherwise whoami: extra operand '/groups'  
cdSystem32 & whoami /groups