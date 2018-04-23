_open=open
import sys,os
# 
sfp=r'd:\test\pyhelp\\';sf,sn,sp='','',''
bprint=False;browser=True

def helpc():
	print 'pyhelp  obj [package] [-s :print to screen] [-b :No browser]'

def cmdargs():
	global sf,sfp,sn,sp
	from sys import argv
	if(len(argv)<2):helpc();exit()		
	ls=[]
	for i in argv[1:]:
		# U.msgbox(bprint,browser,i)
		if(len(i)>0):
			if(i[0]!='-'):ls.append(i);continue
			if(len(i)<1):continue
			i=i.lower() 
			if(i[1]=='s'):bprint=True	
			if(i[1]=='b'):browser=False
	if(len(ls)<1 or len(ls)>2):helpc();exit()
	sp,sn=ls[-1],ls[0]
	sf=sfp+sn+'.html'

def check():
	try:
		exec('import '+sp)
		exec('from %s import *'%sp)
	except Exception as err:
		if(str(err).find('invalid syntax (<string>, line 1)')>-1):print 'No module named '+sp
		print err
		exit()
		
def display():
	os.system('''mkdir '''+sfp)
	from qgb import U,T
	U.setOut(sf)
	print '<textarea style="width:100%; height:100%;">'
	exec('from %s import *;help(%s)'%(sp,sn))
	print '</textarea>'
	U.resetOut()
	print 233
	# if(browser):os.system('''start "" '''+sf)

	# if(bprint):
		# print _open(sf).read()[43:-13]
		

		
if(__name__=='__main__'):
	# from qgb i 
	cmdargs()
	# print sn,sp,sf,bprint,browser
	check()
	display()




