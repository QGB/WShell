_open=open
from sys import *
import sys,os
from qgb import U,T


def helpc():
	print 'pyhelp  obj [package] [-s :print to screen] [-b :No browser]'
	
if(len(argv)<2):helpc();exit()		
bprint=False;browser=True

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
sf='d:/test/pyhelp/'+sn+'.html'
def check():
	try:
		exec('import '+sp)
		exec('from %s import *'%sp)
	except Exception as err:
		if(str(err).find('invalid syntax (<string>, line 1)')>-1):print 'No module named '+sp
		print err
		exit()
check()

std,sys.stdout=sys.stdout,open(sf,'w+')
print '<textarea style="width:100%; height:100%;">'
exec('from %s import *;help(%s)'%(sp,sn))
print '</textarea>'
sys.stdout.close()

if(browser):os.system('''start "" '''+sf)

if(bprint):
	sys.stdout=std
	print _open(sf).read()[43:-13]




