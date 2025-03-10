import schedule
import time

# Define the task function
def my_task():
    print("Task is running!")

# Schedule the task to run every 5 seconds
schedule.every(5).seconds.do(my_task)

# Infinite loop to keep the script running and checking for tasks
while True:
    schedule.run_pending()  # Check if there's any task that needs to run
    time.sleep(1)  # Sleep for 1 second to prevent high CPU usage
