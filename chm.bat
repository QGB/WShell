@if "%1"=="" (goto help)

hh.exe -decompile %1 %1.CHM
@goto end

:help
@echo decompress chm file
@echo usage: %0% fileName[.chm]

:end