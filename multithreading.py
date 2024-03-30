import time
import threading

start_itme = time.perf_counter()

def do_something(sec):
    print(f"sleeping for {sec} seconds.....")
    time.sleep(sec)
    print(f"Done sleeping")


if __name__ == "__main__":
    t1 = threading.Thread(target=do_something, args=(2, ))
    t2 = threading.Thread(target=do_something, args=(2, ))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    finish_time = time.perf_counter()
    print(f"Done in {round(finish_time-start_itme, 3)} seconds")
