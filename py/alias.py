import S
a= sys.argv
gim2=2###min short length

def _py():
	if len(a)!=2 or '/' in a[1] or '\\' in a[1] or '.' in a[1]:
		print '-p name illegal(/,\\,.)'
		help_()
	ss=S.p+a[1]+'.bat'
		
	if old(ss):U.pause()
	
	U.write(ss,'''@python %~dp0py/{0}.py %*'''.format(a[1]))
	
	sp=S.py+a[1]+'.py'	
	U.write(sp,'import S\n')
	os.system('npp '+sp)
	exit()
	
gdParms={('-p','-py'):_py}

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
		f=open(a,'r')
		s=f.read()
		f.close()
	except Exception as e:print e;return False
	if len(s)<gim2:return False
	print '-'*10,'old','-'*10
	print s
	print '-'*25
	return True

	
def main():
	def removeP(asp,ai):
		if asp in a:
			a.remove(asp)
			gdParms[ai]()

	for i in gdParms.keys():
		if type(i)==type(()):
			for j in i:removeP(j,i)
		elif type(i)==type(''):removeP(i,i)

	if len(a)==1:help_()
	a[1]=path(a[1])
	ic=25
	if old(a[1]):ic=0

	if len(a)==2:
		print '='*ic,'Input one line cmd:'
		try:
			a.append(raw_input())
			if len(a[2])<gim2:help_()
		except Exception:print Exception
 		
	if len(a)<3:
		help_()

	# os.chdir('..')
	f=open(a[1],'w')
	f.write(a[2])
	f.close()

	print  a[1],'[', a[2],']','sucess!'

main()