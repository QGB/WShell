import sys,os
a= sys.argv
path=os.path

def getShellPath(fileName=''):
	fileName=fileName.replace('\\','/')
	if path.isabs(fileName):
		return fileName
	else:
		p=path.abspath(__file__)
		for i in 1,2:p=path.dirname(p)
		return p.replace('\\','/')+'/'+fileName

	
p=getShellPath()
# print p