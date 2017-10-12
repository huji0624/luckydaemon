#!/usr/bin/python

__version__ = "v1.0"

from daemon import Daemon

class Daemonshell(Daemon):
	def setShell(self,shell):
		self.shell = shell
	def run(self):
		self.shell.runShell()

class Appshell:
	def checkDirs(self):
		dirs = [self.pidPath,self.outPutPath]
		for path in dirs:
			import os
			if not os.path.isdir(path):
				os.makedirs(path)
	@property
	def pidPath(self):
		import os
		return os.path.expanduser('~') + "/pids"

	@property
	def pidFile(self):
		return self.pidPath + "/" + self.cname + ".pid"

	@property
	def outPutPath(self):
		import os
		return os.path.expanduser('~') + "/output"
	@property
	def cname(self):
		return self.__class__.__name__
	def error(self,parser,msg):
		if msg:
			print msg
		parser.print_help()
		exit(1)

	def stop(self):
		import os
		if os.path.isfile(self.pidFile):
			ret = os.system("kill `cat '%s'`" % (self.pidFile))
			if ret == 0:
				print self.cname+" has stopped."
			else:
				print self.cname+" stop error."
		else:
			print self.cname + " is not running."

	def start(self):
		use = '''
			python *.py [start|stop|restart]

		[note]restart is used with release model as default.
		'''
		from optparse import OptionParser  
		parser = OptionParser(use)
		parser.add_option("-m", "--model", dest="model" , help="default is debug.", metavar="release|debug")
		(options, args) = parser.parse_args()
		if len(args)==1:
			action = args[0]
			if action == "start":
				if options.model == "release":
					self.startShell()
				else:
					self.runShell()
			elif action == "stop":
				self.stop()
			elif action == "restart":
				self.stop()
				self.startShell()
			else:
				self.error(parser,"not support action.")
		else:
			self.error(parser,None)

	def startShell(self):
		print "Appshell is about running."
		self.checkDirs()
		outputfile = self.outPutPath + "/" + self.cname + ".out"
		ds = Daemonshell(self.pidFile,stdout=outputfile,stderr=outputfile)
		ds.setShell(self)
		ds.start()

	def runShell(self):
		pass
