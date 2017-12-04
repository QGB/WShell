import S
if len(S.a)!=2:print S.name,'copy:stdinToClipboard , paste:print clipboard'   ;exit()


S.a[1]=S.a[1].lower()

if S.a[1].startswith('c'):
	sin=U.readStdin()
	while(sin.endswith('\n')):
		sin=sin[:-1]
	U.clipboard.set()

if S.a[1].startswith('p'):print U.clipboard.get()
	