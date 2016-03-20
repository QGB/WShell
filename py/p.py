import S

gbcmd=False

def _help():
	print S.name,'pyFile... [-c : open in current console]'
	exit()
if S.a.__len__()==1:
	sys.stdout =open(os.devnull, 'w')
	U.main()
	sys.stdout=sys.__stdout__
	# print 222
	_help()
	
	
if '-c' in S.a:
	S.a.remove('-c')
	gbcmd=True
	
if not S.a[1].lower().endswith('.py'):
	S.a[1]+='.py'
# if 'py' not in S.a[1].lower():_help()
if __name__ == '__main__':
	S.a[0]='python'
	if gbcmd:U.cmd(S.a)
	else:U.run(S.a)