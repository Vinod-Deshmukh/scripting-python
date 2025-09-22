# Script 19 alarm_clock2
import time
import datetime
import playsound 
import os
def set_alarm():
    alram_time_str=input("Enter the time in HH:MM:SS Format")
    # Validate Input Format
    if(alram_time_str!=8 or alram_time_str[2]!=":" or alram_time_str[5]!= ":"):
        raise ValueError("Invalid format.Please use HH:MM:SS format")
    alarm_hour=alram_time_str[0:2]
    alarm_minutes=alram_time_str[3:5]
    alarm_seconds=alram_time_str[6:8]
    