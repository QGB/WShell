#coding=utf-8
#TODO 增加一个选项，把一个命令及其参数  自动转换成 cmdArg1Arg2.bat  ,而不需要指定一个名字。。。这个选项用什么表示比较好？
import S
import sys
from qgb import *
a= sys.argv
gim2=2###min short length
giMax=99
def _py():
	if len(a)!=2 or '/' in a[1] or '\\' in a[1]:
		print('-p name illegal(/,\\,.)')
		help_()
	
	
	write(a[1],'''@python %~dp0py/{0}.py %*'''.format(a[1]))
	sp=S.py+a[1]+'.py'	
	write(sp,'''import S
if len(S.a)==1:print S.name,''   ;exit()

	''')
	U.npp(sp)
	# print sp
	exit()
def _lnk():
	_start(lnk=True)
	
def _start(lnk=False):
	''' a0 stdin.name stdin
		a0 a1 stdin
		a0 a1.name a1
		a0 a1 a2
		
	'''
	start='''@start "" "{0}"'''
	# if U.debug():print a,'\n',U,T,N,F
	# if len(a)==2:
	
	sp=S.getStdinPath()
	if sp :
		sp=S.path.abspath(sp)
		# start=start.format(sp)
	# else:
	
	if len(a)==1:
		if sp:
			a.append(F.getNameWithoutExt(sp))
			a.append(sp)
		else:help_()
	if len(a)==2:
		if sp:a.append(sp)
		else:
			a[1]=T.sub(U.getCmd(),S.a[0],'').strip()#忽略空格路径影响
			# U.ipy()
			a[1]=S.path.abspath(a[1])
			a.append(a[1])
			if U.debug():print(a,F.getNameWithoutExt(a[1])  )
			a[1]=F.getNameWithoutExt(a[1])
	if len(a)==3:		
		a[1]==path(a[1])
		a[2]=S.path.abspath(a[2])
		
		if S.path.exists(a[2]):
			if lnk:
				a[2]='"{}"'.format(a[2])
			else:
				a[2]=start.format(a[2])
		else:
			help_()
	# if '{0}' not in start:
	# a[1]=path(a[1])
	
	write(a[1],a[2])
		
	# else:
		
	exit()	
		
def _cd():
	# print 233333,U.pwd(),S.a
	cd='''@{0}&@cd {1}%*'''
	
	if len(a)==2:
		if not a[1].startswith('cd'):
			a[1]='cd'+a[1]
			print('cd cmd is [',a[1],']')
		if len(a[1])>giMax:
			print(a[1],'Too long ![:%s]'%giMax)
			exit()
			
		p=U.pwd()
		sp='\\'
		p=p.replace('/',sp)
		if not p.endswith(sp):p+=sp
		drive=os.path.splitdrive(p)[0]
		cd=cd.format(drive,p)
		
		write(a[1],cd)
	else:
		help_()
	exit()
	
gdParms={('-p','-py'):_py,('-start','--start','-s','-S'):_start,('-L','-l','-lnk'):_lnk,('-c','-cd','-CD'):_cd}

# print gdParms
# exit()
def help_(msg='alias short [longCmd] '+str(gdParms.keys())):
	print('Help: ',msg)
	print('     ',a,gRemoved_P or '' )
	exit()

def write(name,txt):
	name=path(name)
	if old(name):U.pause()
	# print (name,txt)
	# U.gbPrintErr=False #禁用F.write错误提示
	U.save(F.write(name,txt,autoArgs=False) or help_('can\'t write '+name))  #
	'''U.load()#'False\n'
	#Error  [Errno 22] invalid mode ('wb') or filename: 'G:/QGB/babun/cygwin/home/qgb/wshell/-?.bat'  G:/QGB/babun/cygwin/home/qgb/wshell/-?.bat <pteredor.py >sucess!
	'''
	U.p(name,'<'+txt[:50] )
	if len(txt)>50:
		U.p( '...')
	U.pln( '>sucess!')
	
	
def path(a):
	if len(a)<1:help_()
	a=a.replace('\\','/')
	if a.startswith('.'):
		if '/'==a[1]:
			if '/' not in a[2:]:
				a=os.getcwd()+a[1:]
	
	if not os.path.isabs(a):
		a=S.p+a
		
	# a=a.lower()	
	if not a.endswith('.bat') and '.' not in a:
		a+='.bat' 	
	return a

	
def old(a):
	# print S.a,a
	if not F.exists(a):return False
	s=''
	try:
		s=U.read(a)
	except Exception as e:print e;return False
	if len(s)<gim2:return False
	print('-'*10,'old','-'*10)
	print(s[:100])
	if len(s)>200:
		print('.............')
		print(s[-100:])
	print('-'*25)
	return True

gRemoved_P=[]
def main():
	# print a
	global gRemoved_P
	def removeP(asp,ai):
		if asp in a:
			a.remove(asp)
			gRemoved_P.append(asp)
			gdParms[ai]()

	for i in gdParms.keys():
		if type(i)==type(()):
			for j in i:removeP(j,i)
		elif type(i)==type(''):removeP(i,i)

	if len(a)<=1:help_()
	
	# ic=25
	# if old(a[1]):ic=0      '='*ic,

	if len(a)==2:
		if U.stdin.isatty():
			print('Input one line cmd:')
			try:
				a.append(raw_input())
				if len(a[2])<gim2:raise Exception('input too short!')
			except:help_()
		else:	# if not U.stdin.isatty():
			a.append(U.readStdin())
	else:
		cmd=U.getCmd()
		cmd=T.sub(cmd,'alias.py','').strip()
		cmd=T.sub(cmd,S.a[1],'').strip()
		if cmd:a[2]=cmd
	if len(a)<3:
		help_()		
		
	if '&' in a[2]:a[2]=a[2].strip('"')
	
	if not a[2]:help_(msg='a[2] is null')
	# a[1]=path(a[1])
	# if U.debug():print S.a,a;print U.getCmd()#sys.argv也被修改了
	#a[1] 已经在前面被修改过啦！！
	
	# for i in range(len(a)-3):
		# a[2]+=' '+T.string(a[3+i])		
	write(a[1],a[2])


if __name__=='__main__':main()