import sys,os;sys.path.append('d:\pm');from qgb import *
a= sys.argv
path=os.path

if __name__ == '__main__':U.sleep(1);exit()

frame=sys._getframe().f_back
def __backImport():
	global frame
	g=globals()
	for i in g.keys():
		if type(g[i])==type(sys) :
			frame.f_globals[i]=g[i]
	##################################		
	if '__file__' not in  frame.f_globals.keys():return None
	name=os.path.basename(frame.f_globals['__file__'])
	if '.py' not in name.lower():
		return ''
	return T.sub(name,'','.')
name=__backImport()
#################################################
def getShellPath(fileName=''):
	fileName=fileName.replace('\\','/')
	if path.isabs(fileName):
		return fileName
	else:
		p=path.abspath(__file__)
		for i in 1,2:p=path.dirname(p)
		return p.replace('\\','/')+'/'+fileName

	
p=getShellPath()
py=p+'/py/'
# print p

def info():

	__import__('code').interact(banner="",local=frame.f_globals)
	return

	
	import IPython;IPython.embed(locals=frame.f_locals,globals=frame.f_globals)
