#!/usr/bin/env python
class day():
	kl = ["08.30 - 08.45", "08.45 - 09.30", "09.50 - 10.35", "10.45 - 11.30", "12.15 - 13.00", "13.15 - 14.00", "14.00 - 14.15"]

	def Mandag(self, clock=""):
		#print(clock, "ASS")
		mandag  = ["Runde1", "Matematik", "Dansk1","Dansk2", "IU1", "IU2","Runde2"]
		for lects in mandag:
			inx = mandag.index(lects)
			print(self.kl[inx],lects,end="\n")

	def Tirsdag(self, clock=""):
		tirsdag = ["Runde1", "Matematik", "Dansk","Engelsk", "IU1", "IU2","Runde2"]
		for lects in tirsdag:
			inx = tirsdag.index(lects)
			print(self.kl[inx],lects,end="\n")
	def Onsdag(self, clock=""):
		onsdag  = ["Runde1", "Matematik", "Dansk","Engelsk", "IU1", "IU2","Runde2"]
		for lects in onsdag:
			inx = onsdag.index(lects)
			print(self.kl[inx],lects,end="\n")
	
	def Torsdag(self, clock=""):
		torsdag = ["Runde1", "Matematik", "Idræt1", "Idræt2", "IU1", "IU2","Runde2"]
		for lects in torsdag:
			inx = torsdag.index(lects)
			print(self.kl[inx],lects,end="\n")
	
	def Fredag(self, clock=""):
		fredag  = ["Runde1", "Matematik", "Dansk","Engelsk", "IU", "Runde2"]
		for lects in fredag:
			inx = fredag.index(lects)
			print(self.kl[inx],lects,end="\n")

day = day()
def timer(dag="",NextDay=False, clock="08.30"):
	today = datetime.date.today()
	tomorrow = today + datetime.timedelta(days=1)
	days 	= ["Mon", "Tue", "Wed", "Thu", "Fri"]
	daDays  = ["Man", "Tir", "Ons", "Tor", "Fre"]
	if NextDay == True:
		if tomorrow.strftime('%a') not in days:
			print("showing Mon")
		else:
			print(f"Showing {tomorrow.strftime('%a')}")
	else:
		print(f"showing {dag}")
	if dag in days or dag in daDays and NextDay == False:
		try:
			inx = days.index(dag) 
		except ValueError:
			inx = daDays.index(dag)
		if inx == 0:
			day.Mandag(clock)
		if inx == 1:
			day.Tirsdag(clock)
		if inx == 2:
			day.Onsdag(clock)
		if inx == 3:
			day.Torsdag(clock)
		if inx == 4:
			day.Fredag(clock)
	elif dag not in days or dag not in daDays:
		print(f"Sorry, the day \"{dag}\" does not exist!")
		exit()
	

import sys
import time
import datetime

nowday = time.ctime()[:3]
date = time.ctime()[:10]
timeOfDay = time.ctime()[10:16]

	
_days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
clock = time.ctime()[11:16]


print(f"DATE: {date}\n"
		f"TIME: {timeOfDay}\n")

try:
	userDay = sys.argv[1].capitalize()

	if userDay == "Next":
		if nowday not in _days:
			nowday = "Mon"
		nextDay = _days.index(nowday) +1 
		timer(_days[nextDay], NextDay=True,clock=clock)

	elif userDay != "Next":
		timer(userDay)
except IndexError:
	timer(nowday)

