import S
if len(S.a)==1:print S.name,' url [file]'   ;exit()

url=S.a[1]

if len(S.a)==2:
	name=F.filename(url)
else:
	name=S.a[2]

if F.isFileName(name):name='./'+name

if U.debug():print url,name,N.get(url)

print F.write(file=name,data=N.get(url))

