import S



def _help():
	print S.name,'pyFile...'
	exit()
if S.a.__len__()==1:
	sys.stdout =open(os.devnull, 'w')
	U.main()
	sys.stdout=sys.__stdout__
	# print 222
	_help()
	
# if 'py' not in S.a[1].lower():_help()
if __name__ == '__main__':
	S.a[0]='python'
	U.run(S.a)