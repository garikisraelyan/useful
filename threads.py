import time
import datetime
import threading

def sleep_function(a):
    for i in range(0, a):
        print(datetime.datetime.now())
        time.sleep(1)

sleep_time = 0.5
iteration_num = 10
result = int(sleep_time * iteration_num)
functional_thread = threading.Thread(target=sleep_function, args=(result,))
functional_thread.start()

for i in range(0, iteration_num):
    print(i)
    time.sleep(sleep_time)
