# import S
# if len(S.a)==1:print S.name,''   ;exit()

import sys,os;sys.path.append('d:\pm');from qgb import *

# U.click()
import pythoncom
import pyHook

t=U.time()

def onMouseEvent(event):
	# if (U.time()-t)<1:return True
	# else:globals()['t']=U.time()
	
	print "MessageName:", event.MessageName
	# print "Message:", event.Message
	# print "Time:", event.Time
	# print "Window:", event.Window
	# print "WindowName:", event.WindowName
	# print "Position:", event.Position
	# print "Wheel:", event.Wheel
	# print "Injected:", event.Injected
	U.pln( U.stime())
 
	return True

# for i in xrange(1234567):onMouseEvent(None)	
	
# exit()
hm = pyHook.HookManager()

# hm.KeyDown = onKeyboardEvent
# hm.HookKeyboard()

hm.MouseAll = onMouseEvent
# hm.HookMouse()

pythoncom.PumpMessages()