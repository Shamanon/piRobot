#!/usr/bin/python3
# PiRobot System service


if __name__ == '__main__':

	import time, os, systemd.daemon as d, signal, sys

	print('Starting Robot...')

	#This will capture sigint
	def handle_ctrl_c(signal, frame):
		sys.exit(0)
	signal.signal(signal.SIGINT, handle_ctrl_c)
		
	## initialize robot system functions ##

	# LCD
	os.system('/robot/bin/LCD/sys-info &')
	d.notify('STATUS=LCD Activated')
	# PS3 Controller
	# os.system('/robot/bin/controller/ps3-control &')
	# d.notify('STATUS=PS3 Controller Activated')
	# Sound Buzzer
	os.system('/robot/bin/buzzer/buzzer -s72 -n16 r2d2')

	# notify systemd that we're ready
	d.notify('READY=1')
	
	# log date and time
	with open("/robot/log/info", "a") as f:
		f.write("Robot activated @ " + time.strftime('%H:%M %m/%d/%Y ') + '\n')
		f.close()
	
	# main loop	
	while True:
		d.notify('STATUS=Your Robot is Running')
		time.sleep(30)
		
