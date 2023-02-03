#!/usr/bin/env python
# coding: utf-8

# # Start the Python interpreter and use it as a calculator.
# 
# 
# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

# In[3]:


kilometer = float(input("Enter Kilometer Value: "))
miles = 0.6214 * kilometer
print(miles, "miles")

mile = float(input("Enter Mile Value: "))
kilometer = 1.61 * mile
print(kilometer, "kilometer")


# How many seconds are there in 42 minutes 42 seconds?

# In[3]:


hour = float(input("How many hours? "))
minute1 = 60 * hour
minute2 = float(input("How many minutes? "))
seconds = float(input("How many seconds? "))
cummulative_seconds = seconds + (60 * (minute1 + minute2))
print("There are", cummulative_seconds, "seconds overall")


# If you run a 10 kilometer race in 42 minutes 42 seconds,
# What is your average pace (time per mile in minutes and seconds)?
# What is your average speed in miles per hour?

# In[5]:


race_kilometer = float(input("How much distance in kilometers for your race? "))
hour = float(input("How many hours? "))
minute = float(input("How many minutes? "))
seconds = float(input("How many seconds? "))

miles = 0.6214 * race_kilometer
time_s = seconds + (60 * minute)
time_m = (seconds/60) + minute

average_pace_s = miles/time_s
average_pace_m = miles/time_m

print("The average pace per seconds is ", average_pace_s, "miles per seconds while the average pace per minute would be ", average_pace_m, "miles per minute")

time_h = (seconds/3600) + (minute/60) + hour
average_speed = miles/time_h
print("The average speed per second is ", average_speed, "miles per hour")


# In[ ]:




