import sys,os
qpsu=os.getenv('QPSU') or 'd:\pm'
# print [qpsu]
sys.path.append(qpsu[:-4]);from qgb import *
a= sys.argv
path=os.path
stdin=sys.stdin



def es(a):
	if type('')!=type(a) or len(a)<1:return ''
	
	
	# print U.cmd('es',a)
	import subprocess as sp
	
	print sp.Popen(('cmd','/k','es','*qgb\\U.py'))
	
	U.x()

# if __name__ == '__main__':
	# es('*qgb\\U.py')



# if __name__ == '__main__':U.sleep(1);exit()

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


def autoPath(a):
	pass


def getStdinPath():
	sin=U.readStdin();tmp=''
	if not sin:return
	if '\n' in sin:
		for i in sin.split('\n'):
			i=path.abspath(i)
			if ':\$RECYCLE' in i:tmp=i;continue
			if path.exists(i):return i
		return tmp
	sin=path.abspath(sin)
	if path.exists(sin):return sin
	
	return ''
	
def stdinToa():
	sp=getStdinPath()
	if sp and len(a)<3:
		a.append(sp)
		return True
	return False
# print getStdinPath()
# U.exit()
	
	
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
