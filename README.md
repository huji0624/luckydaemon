# luckydaemon
a python daemon wrapper.

1.clone luckydaemon to your dir.

2.create a daemon program.
<code>
  #/usr/bin/python

from luckydaemon.appshell import Appshell

class SomeDaemonApp(Appshell):
        def runShell(self):
                print "hhh"

pt = SomeDaemonApp()
pt.start()

 </code>
