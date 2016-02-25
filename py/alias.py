import sys,os
a= sys.argv
gim2=2
def help_():
	print 'alias short [longCmd]'
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
		p=os.path.abspath(__file__)
		for i in 1,2:p=os.path.dirname(p)
		p=p.replace('\\','/')
		a=p+'/'+a	
		
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