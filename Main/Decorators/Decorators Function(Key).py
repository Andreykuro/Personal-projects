# Define a decorator function that measures the execution time of a function
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.2f} seconds to execute.")
        return result
    return wrapper

# Apply the timing_decorator to a function
@timing_decorator
def slow_function():
    # Simulate a slow computation
    time.sleep(2)
    print("Function executed!")

# Call the decorated function
slow_function()
