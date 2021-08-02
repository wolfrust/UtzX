import os
from time import sleep
try:
	import keyboard
except ModuleNotFoundError:
	os.system("pip install keyboard")
	sleep(5)
	import keyboard

print("Okay, open the window")
sleep(15)
i = 0

def init():
	keyboard.write("pls daily")
	keyboard.press_and_release('enter')

def highlow():
	keyboard.write("pls hl")
	keyboard.press_and_release('enter')
	sleep(3)
	keyboard.write("low")
	keyboard.press_and_release('enter')
	#sleep(3)
	#keyboard.write("pls dep all")
	#keyboard.press_and_release('enter')

def postmeme():
	keyboard.write("pls postmeme")
	keyboard.press_and_release('enter')
	sleep(3)
	keyboard.write("f")
	keyboard.press_and_release('enter')
	sleep(3)

def beg():
	keyboard.write("pls beg")
	keyboard.press_and_release('enter')

def dep():
	keyboard.write("pls dep max")
	keyboard.press_and_release('enter')

def fish():
	keyboard.write("pls fish")
	keyboard.press_and_release('enter')

def hunt():
	keyboard.write("pls hunt")
	keyboard.press_and_release('enter')


init()
while i == 0:
	fish()
	sleep(2)
	hunt()
	sleep(2)
	beg()
	sleep(2)
	postmeme()
	sleep(2)
	highlow()
	sleep(23)
	highlow()
	sleep(23)
	highlow()
	sleep(23)
	highlow()
