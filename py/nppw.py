#coding=utf-8
import sys;'qgb.U' in sys.modules or sys.path.append('G:/QGB/babun/cygwin/lib/python2.7/');from qgb import *;C=c=U.clear;NPP=npp=U.npp
from pywinauto import Application
app=Application()

gsTitle='- Notepad++'
gColour={0x0000ff : 'red' ,
		 0x00ff00 : 'green' ,
		 0x00ffff : 'yellow' ,
		 0xff0000 : 'blue' ,# blue color (RGB = 0x0000FF).
		 0xff00ff : 'pink' ,#应该是 Magenta 洋红 On computer screens, it is made by mixing equal amounts of blue and red
		 0xffff00 : 'cyan' ,#Cyan is a greenish-blue color. 青色
		 0xffffff : 'white' ,}
glc=list( gColour.keys())


hs= [i[0] for i in Win.getAllWindows() if gsTitle in i[1] ]

if len(hs)!=1:raise EnvironmentError('sould only one npp',hs)

app=app.Connect(handle=hs[0])
ws=app.windows()
for i in ws:
	txt=i.window_text()
	if gsTitle in txt:wm=i
	#'剪贴板历史记录'
	if u'\u526a\u8d34\u677f\u5386\u53f2\u8bb0\u5f55' == txt:
		wc=i
		break
	if u'Clipboard History' in txt:
		wc=i
es=wc.element_info.children()

for i in es:
	if i.class_name== u'ListBox':
		elb=i
lb=wc.backend.generic_wrapper_class(elb)

win32defines=U.py.modules('win32defines')[0]
win32gui    =U.py.modules('win32gui')[0]

gicount=lb.send_message(win32defines.LB_GETCOUNT)#395
gicountM=   win32gui.SendMessage(lb.handle, 395, 0, 0)
gicountQ=Win.user32.SendMessageW(lb.handle, 395, 0, 0)
U.pln(lb.item_count(),gicount,gicountM,gicountQ)

#
LB_SETSEL               = 0x0185
LB_SETCURSEL            = 0x0186
LB_GETSEL               = 0x0187
LB_GETCURSEL            = 0x0188
LB_GETTEXT              = 0x0189
LB_GETTEXTLEN           = 0x018A
LB_GETCOUNT             = 0x018B
LB_SELECTSTRING         = 0x018C
LB_DIR                  = 0x018D
LB_GETTOPINDEX          = 0x018E














