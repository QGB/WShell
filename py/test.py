la=[2,3,[2,1,4,5,6],1,8]

for i in range(len(la)):
	
	try:
		la.extend(la[i])
		la.remove(la[i])
	except:pass
	print i
# la.remove(1)
print la




exit()
import sys,os;sys.path.append('d:\pm');from qgb import *

sdo='''<li><a href="javascript:;" class="subdomain_change">.esy.es</a></li>
<li><a href="javascript:;" class="subdomain_change">.16mb.com</a></li>
<li><a href="javascript:;" class="subdomain_change">.96.lt</a></li>
<li><a href="javascript:;" class="subdomain_change">.hol.es</a></li>
<li><a href="javascript:;" class="subdomain_change">.pe.hu</a></li>
<li><a href="javascript:;" class="subdomain_change">.890m.com</a></li>
'''.split("subdomain_change")
ldo=[]
for i in sdo:
	ldo.append(T.sub(i,'>.','</a'))
ldo.remove('')


print ldo,

for i in ldo:
	N.http(i)























ft=('png','doc','xls','ppt')
# ft=(ft,)
# ft=(ft,)
# ft=(ft,)
gt=(1,2,3)

gt=(gt,4)



ft=a=['q','w','e',['r']]



def flapt(x,y):
	def rn(a,b):
		if a==() and b==():return
		if a==():return b
		if b==():return a
		return a,b
		
		
	if type(x)==type(y)==type(()):
		return rn(x,y)
		
	if type(x)==type(()):
		return rn(x,(y,))
	if type(y)==type(()):
		return rn((x,),y)
	return x,y

		
	
	


def flap(*a):
	print reduce(flapt, a)

def foo(*a):
	pass
	
foo(1,(2,3,4,()))	


	# if isinstance(a, list):return sum(a,[])
	# if isinstance(a, tuple):return sum(a,())
	
	
# print foo(ft)

exit()









import S

S.U.exit()


def check(a):
	if type(a).__name__=='method-wrapper':print 'method-wrapper'
	# if typex

# print S.getStdinPath()
s=''
# U.sh
for i in dir(s):
	if i.startswith('__'):
		print '*'*55
		a=eval('s.'+i)
		if callable(a):
			try:print i+'()' ,'[',a(),']'
			except Exception as e:
				help(a);continue;
				U.repl()
		else:
			print i ,a
		
