import multiprocessing
import os

def worker1():
    print(f"The id of process running ID1: {os.getpid}")

def worker2():
    print(f"The id of process running ID2: {os.getpid}")

def worker3():
    print(f"The id of process running ID3: {os.getpid}")

def worker4():
    print(f"The id of process running ID4: {os.getpid}")

def worker5():
    print(f"The id of process running ID5: {os.getpid}")

def worker6():
    print(f"The id of process running ID6: {os.getpid}")

def worker7():
    print(f"The id of process running ID7: {os.getpid}")

def worker8():
    print(f"The id of process running ID8: {os.getpid}")

def worker9():
    print(f"The id of process running ID9: {os.getpid}")

def worker10():
    print(f"The id of process running ID10: {os.getpid}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker1)
    p2 = multiprocessing.Process(target = worker2)
    p3 = multiprocessing.Process(target = worker3)
    p4 = multiprocessing.Process(target = worker4)
    p5 = multiprocessing.Process(target = worker5)
    p6 = multiprocessing.Process(target = worker6)
    p7 = multiprocessing.Process(target = worker7)
    p8 = multiprocessing.Process(target = worker8)
    p9 = multiprocessing.Process(target = worker9)
    p10 = multiprocessing.Process(target = worker10)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()

    print(f"the id of processs p1: {p1.pid}")
    print(f"the id of processs p1: {p2.pid}")
    print(f"the id of processs p1: {p3.pid}")
    print(f"the id of processs p1: {p4.pid}")
    print(f"the id of processs p1: {p5.pid}")
    print(f"the id of processs p1: {p6.pid}")
    print(f"the id of processs p1: {p7.pid}")
    print(f"the id of processs p1: {p8.pid}")
    print(f"the id of processs p1: {p9.pid}")
    print(f"the id of processs p1: {p10.pid}")

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()

    print("Done!")