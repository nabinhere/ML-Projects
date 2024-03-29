import multiprocessing

result = []

def square(mylist):
    global result

    for num in mylist:
        result.append(num*num)

    print(f"Result in process p1: {result}")

if __name__ == "__main__":
    my_list = [1,2,3,4]
    p1 = multiprocessing.Process(target = square, args=(my_list, ))
    p1.start()
    p1.join()
    print(f"Result in the main program: {result}")