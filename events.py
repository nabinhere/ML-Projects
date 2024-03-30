import time
import threading

event = threading.Event()
c=0

def time_tracker1():
    while True:
        time.sleep(5)
        event.set()
        print("event set")

def time_tracker2():
    global c
    while True:
        if event.is_set():
            c= c+2
            print(f"result = {c}")
            event.clear()
            print("event cleared by tracker1")

t1 = threading.Thread(target=time_tracker1)
t2 = threading.Thread(target=time_tracker2)
t1.start()
t2.start()

