import time
# **************************************


# epoch = a date and time from which a computer measures system time
# All this measure from epoch
print(time.ctime(0)) # Since this date (seconds)
print("\n")

# Date after '100000' seconds epoch
print(time.ctime(100000))
print("\n")

# Actual date
print(time.ctime())
print("\n")

# Return current seconds since epoch
print(time.time())
print("\n")

# Another form to return current date
print(time.ctime(time.time()))
print("\n")

# The 'localtime()' method will create a time object based on the current time
# Is made up of different keyword arguments, Example: tm_yday = 248 / The day of of the current year
print(time.localtime())
print("\n")

time_object = time.localtime()
# strftime = string format time
# time.strftime(format, object)

# Check documentation https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior Format Codes
# Format Dates
format_time = time.strftime("%A - %d/%B/%Y - %H:%M:%S" , time_object)
print(format_time)
print("\n")

# Get (UTC) Coordinated Universal Time time
"""El Tiempo Universal Coordinado (UTC) es una escala 
de tiempo que se mantiene en laboratorios de tiempo alrededor 
del mundo y se determina mediante relojes atómicos de alta precisión. 
Se basa en el año gregoriano actual y se encuentra en la latitud 0°, 
el Meridiano Primero (también conocido como Meridiano de Greenwich)."""
print(time.gmtime())
print("\n")

# time.strptime()
# This method parse a string representation of a time and or date and
# return a time object

#time.strptime(string, format)

time_string = "17 January 2012"
# format & string must be in the same order / format or it won't work
time_interpretation = time.strptime(time_string, "%d %B %Y")
print(time_interpretation)
print("\n")


# Must follow this formula
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# We can pass up to nine values
time_tuple = (2022, 11, 17, 21, 23, 11, 0, 0, 0)
# Convert a tuple or object into a readable string
time_asctime = time.asctime(time_tuple)
print(time_asctime)
print("\n")

time_mktime = time.mktime(time_tuple)
print(time_mktime) # Return seconds since epoch
