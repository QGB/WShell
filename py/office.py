import S

if len(S.a)==1 and not S.stdinToa():print S.name,'File(doc,xls,ppt...)'   ;exit()

soffice='''D:\Program Files\MicrosoftOffice2003Portable\MicrosoftOffice{0}Portable.exe'''

doffice={'word':('doc','docx'),
'excel':('xls','xlsx'),
'powerpoint':('ppt','pptx')
}


for i in doffice.keys():
	exec('s{0}=soffice.format(i)'.format(i))
	
	

# print sword
# if S.a[1].endswith('doc'):U.run(sword,S.a[1])


