import time

print("\U0001F4A5")
print("\U0001F6A9")


start_time = (time.time())
print(start_time)

time.sleep(63)

stop_time = (time.time())
print(stop_time)

duration = stop_time - start_time
print(duration)

hours = int(duration // 60**2)
mins = int(duration // 60)
secs = round(duration % 60)

print(f"Hours: {hours} Mins: {mins} Seconds: {secs}")