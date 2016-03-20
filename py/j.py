import S
if len(S.a)==1:print S.name,'[file,clasName]';exit()

if len(S.a)==2:
	
	if S.a[1].lower().endswith('.java'):
		S.a[1]=T.subr(S.a[1],'','.')
		
		# print S.a[1]
	