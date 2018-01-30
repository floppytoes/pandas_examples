import sys
import os
import time
import datetime


# look at file and see if datestamp has changed
#   if it has, execute the current version
# this is NOT secure or hardened in any way - nonproduction use only


#print(sys.argv)


if len(sys.argv) == 2:
	file = sys.argv[1]
	file_last_mod_time = 0
	command = "python " + str(file)

	while True:
		file_mod_time= os.stat(file).st_mtime
		time.sleep(.1)

		time_topOfWhile_epoch = time.time() # epoch time
		time_topOfWhile_string = time.strftime("%H:%M:%S")

		now = datetime.datetime.now()  # used???
		#now_str1 = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)  # no 0 padding

		runNow = False
		if file_last_mod_time == 0:
			file_last_mod_time = file_mod_time
			print("----------Initial Run " + time_topOfWhile_string + ": " + command + ": ")
			runNow = True

		if file_mod_time > file_last_mod_time:
			diff = file_mod_time - file_last_mod_time
			print("----------Next Run: " + time_topOfWhile_string + " " + str(round(diff,1)) + " seconds since last: ")
			file_last_mod_time = file_mod_time
			runNow = True

		if runNow:
			time_t0_epoch = time.time() 
			os.system("python " + str(file))
			time_t1_epoch = time.time() 

			time_bottomOfWhile_string = time.strftime("%H:%M:%S")
			print("----------Run Complete:", time_bottomOfWhile_string, "took:", round(time_t1_epoch - time_t0_epoch,2), "seconds\n")




	#print("I found: " + str(sys.argv))
else:
	print("nope")



