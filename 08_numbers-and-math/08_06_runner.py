# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)


total_km = 10 * 1.6
running_time_sec = 30 * 60 + 30
sec_hour = 60 * 60
multiplier = sec_hour / running_time_sec

final_val = total_km * multiplier

print(f"The runner ran at a pace of {final_val} km per hour")







