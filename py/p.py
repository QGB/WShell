import S

gbcmd=False
gsext=['.py','.pyw']
def _help():
	print S.name,'pyFile... [-c : open in current console]'
	exit()
	
	
if S.a.__len__()==1:
	# sys.stdout =open(os.devnull, 'w')
	U.main(display=False,pressKey=True)
	# sys.stdout=sys.__stdout__
	# print 222
	_help()
	
	
if '-c' in S.a:
	S.a.remove('-c')
	if len(S.a)==1:U.cmd('python')
	gbcmd=True

# for i in range(len(S.a)):
	# if i==0:continue
	# if T
S.a[1]=U.autof(S.a[1])

	
if not U.inMuti(S.a[1].lower(),gsext,f=''.endswith):
	S.a[1]+='.py'
# if 'py' not in S.a[1].lower():_help()
if __name__ == '__main__':
	S.a[0]='python'
	if gbcmd:U.cmd(S.a)
	else:U.run(S.a)