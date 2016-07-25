import S
a= sys.argv
gim2=2###min short length

def write(name,txt):
	if old(name):U.pause()
	U.write(name,txt)
	print  name,'[',txt[:33],'...]','sucess!'

def _py():
	if len(a)!=2 or '/' in a[1] or '\\' in a[1]:
		print '-p name illegal(/,\\,.)'
		help_()
	ss=path(a[1])
	
	U.write(ss,'''@python %~dp0py/{0}.py %*'''.format(a[1]))
	
	sp=S.py+a[1]+'.py'	
	write(sp,'''import S
if len(S.a)==1:print S.name,''   ;exit()

	''')
	U.cmd('npp',sp)
	# print sp
	exit()
	
def _start():
	start='''@start "" "{0}"'''
	if len(a)==2:
		sp=S.getStdinPath()
		if sp:
			start=start.format(sp)
			# print start,sp
			
	elif S.path.exists(a[2]):
		start=start.format(S.path.abspath(a[2]))
	if '{0}' not in start:
		a[1]=path(a[1])
		
		write(a[1],start)
	exit()	
		
	
gdParms={('-p','-py'):_py,('-s','-S','-start'):_start}

# print gdParms
# exit()
def help_():
	print 'alias short [longCmd] ',gdParms.keys()
	print a
	exit()

def path(a):
	if len(a)<1:help_()
	a=a.replace('\\','/')
	if a.startswith('.'):
		if '/'==a[1]:
			if '/' not in a[2:]:
				a=os.getcwd()+a[1:]
	
	if not os.path.isabs(a):
		a=S.p+a
		
	a=a.lower()	
	if not a.endswith('.bat'):
		a+='.bat' 	
	return a

	
def old(a):
	if not os.path.exists(a):return False
	s=''
	try:
		U.read(a)
	except Exception as e:print e;return False
	if len(s)<gim2:return False
	print '-'*10,'old','-'*10
	print s
	print '-'*25
	return True

	
def main():
	# print a
	def removeP(asp,ai):
		if asp in a:
			a.remove(asp)
			gdParms[ai]()

	for i in gdParms.keys():
		if type(i)==type(()):
			for j in i:removeP(j,i)
		elif type(i)==type(''):removeP(i,i)

	if len(a)<=1:help_()
	a[1]=path(a[1])
	
	ic=25
	if old(a[1]):ic=0

	if len(a)==2:
		print '='*ic,'Input one line cmd:'
		try:
			a.append(raw_input())
			if len(a[2])<gim2:help_()
		except:U.x()
 	else:
		for i in range(len(a)-3):
			a[2]+=' '+T.string(a[3+i])
	if len(a)<3:
		help_()
		
	# print a
	write(a[1],a[2])


if __name__=='__main__':main()