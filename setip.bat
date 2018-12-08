@if "%1"=="" (goto help)

set adapter=%2
@if "%2"=="" (set adapter='wlan')

qp N.setIP(ip=%1,adapter=%adapter%)
@goto end

:help
@echo %0 Help: 
@echo 	default adapter 'wlan' : 12
@echo 	setip '192.168.2.2'
@echo 	setip 2.2
@echo 	setip 0 # dhcp
: @echo \Tabalabala

:end
