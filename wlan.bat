if "%*"=="" (set wifiName="Buildozer ") ELSE (set wifiName=%*)

sc query "WlanSvc"
net start WlanSvc

netsh interface set interface wlan disable
netsh interface set interface wlan enabled

@REM netsh wlan add profile filename="qgb" > 0
netsh wlan connect name=%wifiName%
