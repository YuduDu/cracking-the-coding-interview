#!/usr/bin/python

#calculate the angle between hour and minute hands
def clock_hands_angle(time):
	# pharse the time
	try:
		time = time.split(":")
		hour = int(time[0])
		minute = int(time[1])
	except:
		return False

	# check hour and minutes
	if (0<=hour<=12) and (0<=minute<60):
		# calculate angle of hour hands
		h =  hour*360/12 + minute*360/12/60
		m = minute*360/60
		#angle 
		angle = abs(h-m)
		if 360>=angle>180:
			angle = 360-angle
		return angle
	else: return False
		
print clock_hands_angle("11:34")			

		