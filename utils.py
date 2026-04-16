import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timeit
def compute_heavy_task(n):
    total = 0
    for i in range(n):
        total += sum(j ** 2 for j in range(1000))
    return total

@timeit
def optimize_data_processing(data):
    unique_data = set(data)
    processed_data = {element: data.count(element) for element in unique_data}
    return processed_data

if __name__ == "__main__":
    print(compute_heavy_task(5))
    sample_data = [1, 2, 2, 3, 3, 3]
    print(optimize_data_processing(sample_data))