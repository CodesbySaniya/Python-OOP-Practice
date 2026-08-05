import time

def timer(func):

    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print(end - start)

    return wrapper


@timer
def work():

    print("Working...")
    time.sleep(2)

work()
