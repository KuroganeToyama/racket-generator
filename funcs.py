# Sums up all the numbers in num_list
def add(num_list):
    sum = 0
    for num in num_list:
        sum = sum + num
    return sum

# Find the median of all numbers in num_list
def median(num_list):
    median = 0
    sorted_list = sorted(num_list)
    length = len(sorted_list)
    
    if length % 2 == 0:
        mid1 = sorted_list[length // 2 - 1]
        mid2 = sorted_list[length // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_list[length // 2]
    
    return median