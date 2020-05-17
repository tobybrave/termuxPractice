import time
import datetime

#time
def countdown(stop):
    while True:
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            print("Good bye!")
            break
        print('The count is: '
              + str(difference.days) + " day(s) "
              + str(count_hours) + " hour(s) "
              + str(count_minutes) + " minute(s) "
              + str(count_seconds) + " second(s) "
              )
        time.sleep(1)


end_time = datetime.datetime(2020, 5, 10, 2, 5, 30)
countdown(end_time)
 
        

#file.close()
#Datatime.now
print(time.ctime())
print(datetime.datetime(2020, 6, 1) -datetime.datetime.now())