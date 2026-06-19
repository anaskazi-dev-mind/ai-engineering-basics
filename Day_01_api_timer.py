import time 

def time_it(func):

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Function takes {end_time - start_time} seconds.")

    return wrapper

@time_it
def fake_api_call():
    print("Fetches data from the API.")
    time.sleep(2)
    print("Done")


fake_api_call()

