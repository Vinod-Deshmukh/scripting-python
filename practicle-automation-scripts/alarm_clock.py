# Script 19 Simple Alarm Clock – Alert at user-given time.
# import datetime, time.
# Input alarm time (HH:MM).
# While loop → check current time
# Read the code Understood all but strftime("%H:%M:%S") this 
import datetime
import time
import os

# You might need to install playsound: pip install playsound
try:
    from playsound import playsound
except ImportError:
    print("playsound module not found. Install it using 'pip install playsound' to enable sound alerts.")
    playsound = None

def set_alarm():
    """Sets an alarm and plays a sound when the specified time is reached."""
    while True:
        try:
            alarm_time_str = input("Enter alarm time (HH:MM:SS): ")
            # Validate input format
            if len(alarm_time_str) != 8 or alarm_time_str[2] != ':' or alarm_time_str[5] != ':':
                raise ValueError("Invalid time format. Please use HH:MM:SS.")
            
            alarm_hour = int(alarm_time_str[0:2])
            alarm_minute = int(alarm_time_str[3:5])
            alarm_second = int(alarm_time_str[6:8])

            if not (0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59 and 0 <= alarm_second <= 59):
                raise ValueError("Invalid time values. Hour (0-23), Minute (0-59), Second (0-59).")
            
            break # Exit loop if input is valid
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    print(f"Alarm set for {alarm_time_str}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time_str:
            print("Wake Up! Alarm ringing!")
            if playsound:
                # Replace 'alarm_sound.mp3' with your actual sound file
                # Ensure the sound file is in the same directory as the script
                # or provide the full path.
                try:
                    playsound('osho.mpeg') 
                except Exception as e:
                    print(f"Error playing sound: {e}")
            break
        time.sleep(1) # Check every second

if __name__ == "__main__":
    # Create a dummy sound file if playsound is available and the file doesn't exist
    if playsound and not os.path.exists('osho.mpeg'):
        print("Note: 'alarm_sound.mp3' not found. Create or place an MP3 file with this name for sound alerts.")
    
    set_alarm()