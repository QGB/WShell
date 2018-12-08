#coding=utf-8
import S
Win=U.Win
# print U.Win
# print T.printAscii
# Win.getCmdLine=getCmdLine
cmd= Win.getCmdLine()
r= F.getPaths(cmd)
# U.log(r)
for i,v in enumerate(r):
	# print U.getShellPath(),v
	if U.gsw in v:
		if U.gst in r:continue
		v=r[i]=U.gst

	if '&' not in v[:3]:
	#  gst path no space ,  otherwise err in bat @set "gst=.."".. "
		r[i]='{0}&cd {1}'.format(v[:2],v)
# r=U.delMuti(r)
# for i in rZ
if r:
	# U.msgbox(r)
	U.p(r[-1])
else:
	v=U.gst
	U.p('{0}&cd {1}'.format(v[:2],v)   )
# U.log(r)

exit()
def getPaths(a):
	rlist=[]
	j=0
	PATH_NAME= T.PATH_NAME.replace(':','')
	for i,v in enumerate(a):
		if i<j:continue
		if v==':':
			i0=0
			vn=a[i-1:]
			r=''
			lastVs=False
			colon=False
			for j,v in  enumerate(vn):
				if v not in PATH_NAME  :
					if v==':':
						if not colon:continue#首次出现 ，继续
						colon=True

					if F.isdir(r+vn[i0:j]):
						r+=vn[i0:j]
					else:
						r+=vn[i0:j-1]
					r=r.strip()
					break;
						
				if v in ('/','\\'):
					if lastVs:
						i0+=1
					else:
						r+=vn[i0:j]+'/'
						if F.exist(r):# and F.isdir(r):
							i0=j+1		
						else:
							r=vn[:-(j-i0)].strip()
							break
					lastVs=True
				else:
					lastVs=False	
			j=i+j
			if r:rlist.append(r)
	return rlist
U.msgbox(getPaths(cmd),cmd)
U.x(22)	
def getPath(cmd,start=None):
	'''if start!=None: return path,EndIndex'''
	cmd=cmd[start:]
	for i,v in enumerate(cmd):
		if v==':':
			i=i-1
			break
		i=-1
	cmd=cmd[i:]
	if not cmd:
		if start==None:return ''
		else:          return (),-1
			# Win.msgbox(Win.getCmdLine(),'Not found cd path');exit()
	
	i0=0
	lastVs=False
	r=''
	for i,v in  enumerate(cmd):
		if v not in T.PATH_NAME:
			if F.isdir(r+cmd[i0:i]):
				r+=cmd[i0:i]
				if start==None:return r
				else:          return r,i
				
		# U.msgbox( r,cmd,i0,i)
		if v in ('/','\\'):
			if lastVs:
				i0+=1
			else:
				# U.msgbox( r,cmd,i0,i)
				r+=cmd[i0:i]+'/'
				if F.exist(r):# and F.isdir(r):
					i0=i+1
				else:
					r=r[:-(i-i0)]
					if start==None:return r
					else:          return r,i
			lastVs=True
		else:
			lastVs=False
	# U.p(r,cmd,i0,i,lastVs,split=',')
	if start==None:return ''
	else:          return '',-1
	
# print 111111,getPath(cmd,5),U.msgbox()#print 无效/？？？？？？？/
U.p(cmd,getPath(cmd,15))

i=5
while True:
	r,i=getPath(cmd,i)
	# U.msgbox( r,cmd,i)
	if not r:break
	if U.gsw[:-1] in r:
		continue
	else:
		print r
		exit()
print U.gst
# F.exist('g://test/////ipy')
# Out[16]: True
# if len(S.a)<=1:exit()

# print r,cmd,i0,i
# if S.a[1][1]==':':
	# p=os.path.dirname(S.a[1])
	# os.chdir(p)
	# os.system('d:&cd pm')
	# print os.getcwd()
	