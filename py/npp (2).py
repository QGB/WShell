#coding=utf-8
import S

sf=r'C:\Users\Administrator\AppData\Roaming\Notepad++\notepad++.exe'
if not os.path.exists(sf):
	sf1=r':\QGB\npp\notepad++.exe'
	sf2=r''':\Program Files\Notepad++\notepad++.exe'''
	for i in 'cdefgq':
		# i+=sf
		if os.path.exists(i+sf1):
			sf=i+sf1
			break
			
		if os.path.exists(i+sf1):
			sf=i+sf2
			break
		
			
			
if len(S.a)==1:
	sin=U.getStdin().strip()
	r=F.getPaths(sin)
	
	
	if sin and os.path.exists(sin):S.a.append(sin)#从管道获取文件名并打开
	elif len(sin)>3:#从管道获取数据保存到临时文件
		U.cdt()
		U.cd('npp',mkdir=True)
		tmp=U.pwd()+U.stime(ms=False)+'.txt'
				
		S.a.append(tmp)
		U.save(U.write(tmp,sin,autoArgs=False))
				
		# U.cdt()
		# st=U.read(tmp)
		# print len(st),len(sin),st==sin
		# U.write('1.txt',st)
		
		
		# print U.md5(sin) 
		# exit()
		# U.write(S.a[-1],sin)
	
if len(S.a)<2 or not S.a[1]:
	try:
		value,file=U.load(returnFile=True)
	except Exception as e:
		'''没有读取到save value'''
		if U.debug():print e,U.load(returnFile=True)
		value=''
		# if U.DEBUG:U.repl()
		#因为本文件一次性运行，所以基本不会有DEBUG 机会。。
	if F.exist(value):
		S.a=[sf,value]
		U.pprint( U.renameDictKey(F.ll(value),new='npp U.load')) 
	else:
		print('Help: stdin | npp [FileName...]')
		os.startfile(sf)
		exit()
###############################
else:
	S.a[0]=sf
	S.a[1]=F.autof(S.a[1])
	if F.isDir(S.a[1]):# npp打开文件夹时默认打开所有文件
		U.pprint(F.ls(S.a[1]))
		U.pause('!!! Would you like open these?    Ctrl+C to break')

print S.a
U.run(S.a)