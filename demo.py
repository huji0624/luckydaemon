#!/usr/bin/python
from appshell import Appshell

class Demo(Appshell):
	def runShell(self):
		while True:
			print "demo run"
			import time
			time.sleep(1)

demo = Demo()
demo.start()