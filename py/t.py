import pprint
def foo():
	print 2333

def te():
	foo=True
	from qgb import U,T
	ls=['globals','vars','locals']
	pprint.pprint(dir())
	for i in ls:
		exec('''U.dicthtml('{0}.html',{0}())'''.format(i))
		
	
te()

# 
# print globals()
# 


