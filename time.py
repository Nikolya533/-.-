import time
start_time_Guru99 = time.time
print("Time elapsed after some level wait...")
print("The start time is",start_time_Guru99)
print("The start time in human form",time.ctime(start_time_Guru99))
time.sleep(1)
end_time_Guru99 = time.time()
print(time.ctime(time.time()))
print("The end time is", end_time_Guru99)
print("The start time in human form",time.ctime(end_time_Guru99))
print("Time elapsed in this example code: ",end_time_Guru99 - start_time_Guru99)