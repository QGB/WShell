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
		S.a.append(U.gst+T.string(U.time())+'.txt')
		
		U.cdt()
		st=U.read('1466078064.42.txt')
		print len(st),len(sin),st==sin
		U.write('1.txt',st)
		U.write('sin.txt',sin)
		
		
		print U.md5(sin) 
		exit()
		U.write(S.a[-1],sin)
	
	if len(S.a)<2 or not S.a[1]:	
		print 'npp FileName...'
		os.startfile(sf)
		exit()

S.a[0]=sf
S.a[1]=U.autof(S.a[1])

print S.a
U.run(S.a)