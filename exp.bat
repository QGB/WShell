@if "%1"=="" (goto curr)
@rem : explorer "C:\Program Files\qBittorrent\"  路径中含有 / 无法正确执行 
: bat要用 gb2312编码保存,换行选择 CR LF，不然 utf-8执行出错

@start "" explorer "%*"
cd "%*"
: 参数为相对路径时 先cd会导致 后start 找不到路径


@goto end

:curr
@start "" explorer .

:end
