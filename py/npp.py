import S
sf=r''':\Program Files\Notepad++\notepad++.exe'''
for i in 'cdef':
	i+=sf
	try:
		os.path.getsize(i)
		sf=i
	except Exception as e:
		pass
		# print e
# exit() 
if len(S.a)==1:
	print 'npp FileName...'
	os.startfile(sf)
	exit()

S.a[0]=sf
U.run(S.a)