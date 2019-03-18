import sys,os,platform
def iswin():
	if platform.system().startswith('Windows'):return True
	else:return False
glnix=['nix','linux','darwin']
def isnix():
	return [i for i in glnix if i in platform.system().lower()]
	# return one_in('nix','linux','darwin',platform.system().lower())
def istermux():
	return 'com.termux' in sys.executable

def iscyg():
	return 'cygwin' in  platform.system().lower()
	
def exists(path):
	if os.path.exists(path):
		return path
	else:
		return ''
qpsu=os.getenv('QPSU') 
if not qpsu:
	if iswin() or iscyg():qpsu=r'%QGB%babun\cygwin\bin\qgb'
	if isnix():qpsu=exists(os.getenv('HOME')+'/qgb') or exists('/root/qgb')
	if istermux():
		qpsu=exists('/sdcard/!/qgb') or exists(os.getenv('HOME')+'/qgb') or exists('/sdcard/qgb') 
sys.path.append(qpsu[:-4])
try:
	from qgb import *
	sys.path.pop()
except Exception as e:
	import pdb;pdb.set_trace()
	raise Exception('#error import qgb in S.py',e)
	from pprint import pprint
	p=os.getenv('conda')
	# pprint(p[:-1] in sys.path)
	def copy(source,destination,fliter={},ext='',no=''):
		'''-v, --invert-match        select non-matching lines'''
		try:os.mkdir(destination)
		except:pass
		source=source.replace('\\','/')
		destination=destination.replace('\\','/')
		# if not source.endswith('/'):source+='/'
		if not destination.endswith('/'):destination+='/'
		for root, dirs, files in os.walk(source):
			root=root.replace('\\','/')
			if no in root or no in dirs:continue
			
			for i in dirs:
				try:
					os.mkdir(destination+i)
					if i=='02':__import__('code').interact(banner="",local=locals())
				except:pass
				
			for j in files:
				if j.endswith(ext):
					if root.endswith('/'):f=root+j
					else:f=root+'/'+j
					j=destination+j
					cmd='copy "{0}" "{1}"'.format(f,j)
					print(cmd)
		__import__('code').interact(banner="",local=locals())
	copy(qpsu,p+'qgb',ext='.pyc',no='.git')
	
	

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

	


def es(a):
	if type('')!=type(a) or len(a)<1:return ''
	
	
	# print U.cmd('es',a)
	import subprocess as sp
	
	print( sp.Popen(('cmd','/k','es','*qgb\\U.py'))   )
	
	U.x()

# if __name__ == '__main__':
	# es('*qgb\\U.py')



# if __name__ == '__main__':U.sleep(1);exit()



def __backImport():
	global frame
	g=globals()
	for i in g.keys():
		try:
			if U.isMod(g[i]):# type(g[i])==type(sys) :
				frame.f_globals[i]=g[i]
		except Exception as e:
			# from qgb import U#local variable 'U' referenced before assignment 
			print (e,0),dir(),globals().keys()
			exit()	
	##################################		
	if '__file__' not in  frame.f_globals.keys():return None
	name=os.path.basename(frame.f_globals['__file__'])
	if '.py' not in name.lower():
		return ''
	return T.sub(name,'','.')


def autoPath(a):
	pass



# print p

def info():

	__import__('code').interact(banner="",local=frame.f_globals)
	return	
	import IPython;IPython.embed(locals=frame.f_locals,globals=frame.f_globals)
#####################################
if __name__!='__main__':	
	a= sys.argv
	path=os.path
	stdin=sys.stdin
	p=getShellPath()
	py=p+'/py/'
	frame=sys._getframe().f_back
	if frame.f_code.co_name=='patched_import':frame=frame.f_back#pycharm
	name=__backImport()
	file=name+'.py'
	if iswin():
		cmd=Win.getCmd().strip()
		arg=T.sub(cmd,a[0],'').strip()
#################################################