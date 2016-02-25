import S,os,sys
if len(S.a)<=1:exit()


if S.a[1][1]==':':
	p=os.path.dirname(S.a[1])
	os.chdir(p)
	os.system('d:&cd pm')
	print os.getcwd()