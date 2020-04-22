import datetime

now_time= datetime.datetime.now()
ss = now_time.strftime("%Y_%m_%d_%H_%M_%S")
print(ss)