#coding=utf8
import S
if len(S.a)==1:
	print S.name,'curl <url>:autoSave '   ;exit()
gmax=555
	
url=S.arg
file=T.subLast(url,'/','')
file=F.filename(file)

# https://raw.githubusercontent.com/Rurik/RightClick_AppLocale/b589d4bbd5d623331c147051b2b8b2e14c96e10e/RCAppLocale.py
# https://github.com/Rurik/RightClick_AppLocale/raw/b589d4bbd5d623331c147051b2b8b2e14c96e10e/RCAppLocale.py
if U.all_in('github.com/','/raw/',url):
	url=url.split('/raw/')
	url=[url[0].replace('github.com/','raw.githubusercontent.com/') , url[1]  ]
	url='/'.join(url)

r=U.cmd('curl.exe',url)
try:
	U.pln(r[:gmax],'......' if len(r)>gmax else '','\n=================\n',url,'\nwriteTo',F.write(file,r))
except Exception as e:
	U.pln(url,e)
U.save(U.gst+file)	
	