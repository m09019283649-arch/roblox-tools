import time

class PerformanceTracker:
    def __init__(self):
        self.records = {}

    def start(self, name):
        self.records[name] = time.perf_counter()

    def stop(self, name):
        if name in self.records:
            elapsed_time = time.perf_counter() - self.records[name]
            del self.records[name]
            return elapsed_time
        return None

def optimize_function(func):
    def wrapper(*args, **kwargs):
        tracker = PerformanceTracker()
        tracker.start(func.__name__)
        result = func(*args, **kwargs)
        elapsed_time = tracker.stop(func.__name__)
        print(f'Function {func.__name__} took {elapsed_time:.4f} seconds')
        return result
    return wrapper

@optimize_function
def compute_heavy_operation(data):
    total = 0
    for number in data:
        total += number ** 2  # Example heavy computation
    return total

# Example usage
if __name__ == '__main__':
    data = range(10000)
    compute_heavy_operation(data)