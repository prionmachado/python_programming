import statistics

def calculate_statistics(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    stdev = statistics.stdev(data)
    variance = statistics.variance(data)
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'stdev': stdev,
        'variance': variance
    } 

stats = calculate_statistics([1, 2, 3, 4, 5, 5, 6, 7, 8, 9]) 
print(stats)