# try:
'''
win ping error explanation:https://technet.microsoft.com/en-us/library/cc940095.aspx
'''
import S

default=['127.0.0.1','192.168.2.3','192.168.2.123','192.168.2.141','8.8.8.8','192.168.1.1','192.168.191.1','10.1.1.254','www.w3school.com.cn','www.ccsu.cn',
'qq.com','baidu.com','taobao.com','g.cn','google.com','public-tools.zhihu.com','github.com']

if S.a[-1].startswith('--'):
	S.a[0]=S.a.pop()[2:]+'.exe'
	
# print S.a
# exit()
if len(S.a)==1:print S.a[0][:-4],'(domain,ip,url)';exit()

for i in range(len(S.a)):	
	if '://' in S.a[i]:
		s=T.sub(S.a[i],'://')
		if '/' in s:s=T.sub(s,'','/')
		S.a[i]=s

	if S.a[i].startswith('-'):continue
	
	
	if len(S.a[i])<4:
		for k in default:
			if S.a[i].lower() in k:
				S.a[i]=k
				break
	# try:U.cmd('ping.exe '+s)
	# except:exit()
	# exit()
# print S.a	

U.cmd(S.a)
# except:exit()