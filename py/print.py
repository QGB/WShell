import S

# U.shtml( S.__dict__)
# if len(S.a)==1:print S.name,''   ;exit()
if len(S.a)==2:
	if F.exist(S.a[1]):
		pass
	else:hex(a[1])


	
def hex(a):
	c='';lastc=True
	for i in a:
		if i in T.HEX+'abcdef':
			if lastc:c+=i
			else:
				U.p(c)
				c=i
			lastc=True
		else:
			lastc=False
			U.p(i)
		if len(c)==2:U.p(chr(F.DHI[c.upper()]));c=''
	
	U.p(c)
if __name__ == '__main__':
	hex('33-44=55 6677')