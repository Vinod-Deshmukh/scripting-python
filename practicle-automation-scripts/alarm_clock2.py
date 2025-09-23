# Script 19 alarm_clock2
import time
import datetime
from playsound import playsound
import os
def set_alarm():
    while True:
        try:
            alram_time_str=input("Enter the time in HH:MM:SS Format \n")
            # Validate Input Format
            if(len(alram_time_str)!=8 or alram_time_str[2]!=":" or alram_time_str[5]!= ":"):
                raise ValueError("Invalid format.Please use HH:MM:SS format")
            
            alarm_hour=int(alram_time_str[0:2])
            alarm_minutes=int(alram_time_str[3:5])
            alarm_seconds=int(alram_time_str[6:8])

            if not(0 <= alarm_hour <= 23 and 0 <= alarm_minutes <= 59 and 0 <= alarm_seconds <= 59):
                raise ValueError("Invalid time values. Hour(0-23).Minutes(0-59).Seconds(0-59)")
            # Breaks the loop if input is valid
            break
        except ValueError as e:
            print(f"Error {e}.Please try again.")
    print(f"alarm set for: {alram_time_str}")
    
    
    while True:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        if current_time==alram_time_str:
            print("Wake UP!")
            if playsound:
                try:
                    playsound('osho.mpeg')
                except Exception as e:
                    print(f"Error in playing sound: {e}")
            break
    # check every second
        time.sleep(1)
# set_alarm()

if __name__=="__main__":
    #create a dummy sound file if playsound is available and file doesn't exists.
    if playsound and not os.path.exists('osho.mpeg'):
        print("Note:osho.mpeg not found.Create or Place an MP3 file with this name for sound alerts.") 
    
    set_alarm()