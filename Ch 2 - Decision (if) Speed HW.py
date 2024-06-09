"""One cause for speeding is the desire to shorten the time spent
traveling. Create a program that calculates the total amount of time
saved if you are traveling with an average speed that is above the
speed-limit as compared to traveling with an average speed exactly at
the speed-limit. Ask the user for the average speed, speed limit and
distance travelled. Calculate the amount of time saved for the distance
travelled. THE TIME SAVED SHOULD BE REPORTED IN MINUTES"""

# Constant
TIME_IN_MINUTES = 60

# Get User Input
DISTANCE = float(input("Enter the distance in miles."))
SPEED = float(input("Enter your average speed in mph."))
LIMIT = float(input("Enter the speed limit in mph."))

# Calculate Normal Time
TIME = DISTANCE / LIMIT

# Calculate Speeding Time
SPEEDTIME = DISTANCE / SPEED

# Calculate Time in Minutes
SPEEDTIME_MIN = SPEEDTIME * TIME_IN_MINUTES
TIME_MIN = TIME * TIME_IN_MINUTES

# Calculate time saved
SAVED = TIME_MIN - SPEEDTIME_MIN

# Calculate Time Saved
if SPEED > LIMIT:
    SAVED = TIME_MIN - SPEEDTIME_MIN
else:
    print("No time saved.")

print(f'Time taken at speed limit: {TIME_MIN:.2f} minutes')
print(f'Time taken at your speed: {SPEEDTIME_MIN:.2f} minutes')
print(f'Time saved in minutes: {SAVED:.2f} minutes')
