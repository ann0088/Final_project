def my_decorator(func):
    import time

    def time_of_func(a,b,v):
        start_time = time.time()
        print('Time : {} seconds.'.format(time.time() - start_time))
    return time_of_func
