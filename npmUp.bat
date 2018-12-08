@echo off

@rem if not use cmd /c  will break the batch   
@rem npm_qgb.info use LF not CR LF    
cmd /c npm adduser < %QGB%npm_qgb.info
cmd /c npm get registry
cmd /c npm set registry http://registry.npmjs.org


echo auto modifying package.json ...
(
echo ############this end can not be deleted and unable to append any char (^)
echo p='package.json'
echo import json
echo d=json.load(open(p^)^)                        
echo v=d['version']                              
echo ri=v.rindex('.'^)+1                          
echo d['version']=v[:ri]+ str(int(v[ri:]^)+1^)  
echo json.dump(d,open(p,'w'^),indent=1^)
echo print(p,'version',v,'+ 0.0.1 success!'^)#
)|python


npm publish