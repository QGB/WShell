import S
sf=r''':\Program Files\Notepad++\notepad++.exe'''
for i in 'cdef':
	i+=sf
	if os.path.exists(i):
		sf=i
		break

if len(S.a)==1:
	sin=U.getStdin()
	if sin and os.path.exists(sin):S.a.append(sin)
	elif len(sin)>3:
		U.cd('npp')
		S.a.append(T.string(U.time())+'.txt')
		U.write(S.a[-1],sin)
	
	if len(S.a)<2 or not S.a[1]:	
		print 'npp FileName...'
		os.startfile(sf)
		exit()

S.a[0]=sf
S.a[1]=U.autof(S.a[1])

print S.a
U.run(S.a)