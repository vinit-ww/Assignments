import subprocess

def py_xwininfo():
		winId=getCurrentWindId()
		print 'winId=%s'%winId

def getCurrentWindId():
	cmd_1=['xprop','-root']
	cmd_2=['awk','/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}']
	p1=subprocess.Popen(cmd_1, stdout=subprocess.PIPE)
	p2=subprocess.Popen(cmd_2, stdin=p1.stdout,stdout=subprocess.PIPE)
	id=p2.communicate()[0]

	return id

py_xwininfo()	