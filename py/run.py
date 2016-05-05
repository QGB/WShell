import S



ft=('png','doc','xls','ppt')
ft=(ft,)

def expand_list(*nested_list):
	for item in nested_list:
		if isinstance(item, (list, tuple)):
			for sub_item in expand_list(item):
				yield sub_item
		else:
			yield item

def flap(*a):
	t=('png','doc','xls','ppt')

	import itertools
	return itertools.chain.from_iterable(a)
	# return reduce(lambda x,y:x+y, a)


# print list(expand_list(ft))
exit()


if len(S.a)==1 and not S.stdinToa():print S.name,'File',ft   ;exit()

if U.inMuti(S.a[1],ft,func=''.endswith):
	print 2333


U.run(S.a)