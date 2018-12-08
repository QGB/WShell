import S
import alias
if len(S.a)<2:
	print 'unalias name[.bat]'
	# print S.a
	exit()
#todo auto remove ws/py


# U.pprint(U.dir(S))
print S.a,U.pwd(),S.p

name=S.a[1]
if not name.endswith('.bat'):name+='.bat'

name=S.p+name
if alias.old(name):U.pause()

print F.delete(name)