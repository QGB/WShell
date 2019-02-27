#coding=utf-8
import S
gsTitle='- Yandex Browser'
giClickY=34
from qgb import py,Win,U,T,N,F
# U=py.importU()
from pywinauto import Application        
app=Application()
pids=[i[0] for i in Win.getAllWindows() if i[1].endswith(gsTitle) ]
ws=[]
for i in pids:
	i=app.Connect(handle=i)   
	i=i.windows() 
	for w in i:
		if w.WindowText().endswith(gsTitle):
			if w not in ws:ws.append(w)
# F.dill_dump(obj=ws,file='browserGo_ws')	
U.pprint(U.il( ws)  )
if U.ct(ws)==0:Win.setCurPos(giClickY,giClickY)
def istop():
	x,y=Win.getCurPos()
	if y>giClickY*6 or y>ih-9:
		U.pln(iw,ih,i,'Cur:',x,y)
		U.exit()

def click(w,x,y=giClickY):
	istop()
	try:
		w.Maximize()
		r=w.Rectangle()
		if x>(r.right-r.left)-200-65:
			return
		w.click_input(coords=[x,y])
#RuntimeError: Window (hwnd=hwndwrapper.DialogWrapper - 'None', YandexBrowser_WidgetWin_1) is not responding!
	except Exception as e:
		print(e)
		U.sleep(5)
	U.p(x,end=' ')
	U.sleep(1)
iw,ih=Win.getScreenSize()		
for w in ws:#is2  can't print w   UnicodeEncodeError: 'ascii' codec can't encode characters in position 29-33: ordinal not in range(128)
	#range(start, stop[, step]) -> range object
	for i in range(9,iw-200-65,44):  #-200 stop click setting button  
		click(w,i)
		
