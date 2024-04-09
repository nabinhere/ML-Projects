from decorators import timer

@timer
def waste_time(num):
    for _ in range(num):
        sum([num**2 for num in range(1000)])

waste_time(10000)
