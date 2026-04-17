import time
import functools

class PerformanceTracker:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        duration = time.time() - start_time
        print(f'Performance: {self.func.__name__} took {duration:.4f} seconds')
        return result

@PerformanceTracker
def expensive_operation(data):
    total = sum(x * x for x in data)
    return total

@PerformanceTracker
def process_data(data_list):
    results = [expensive_operation(data) for data in data_list]
    return results

if __name__ == '__main__':
    sample_data = [range(10000), range(20000), range(30000)]
    print(process_data(sample_data))