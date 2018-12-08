@REM @echo off


@REM @echo auto modifying package.json. If given package@version argument please modify package Manually...
@REM @(
@REM echo ############this end can not be deleted and unable to append any char (^)
@REM echo p='package.json'
@REM echo import json
@REM echo d=json.load(open(p^)^)                        
@REM echo v=d['version']                              
@REM echo ri=v.rindex('.'^)+1                          
@REM echo d['version']=v[:ri]+ str(int(v[ri:]^)-1 or 1^)  
@REM echo json.dump(d,open(p,'w'^),indent=1^)
@REM echo print(p,'version',v,'To',d['version'],'success!'^)#
@REM )|python


npm unpublish --force %*

@REM npm unpublish --force qgb@0.0.2