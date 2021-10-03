def radix_get_max_length(numbers):
    max_digits = 0
    for num in numbers:
        digit_count = radix_get_length(num)
        if digit_count > max_digits:
            max_digits = digit_count
    return max_digits
def radix_get_length(value):
    if value == 0:
        return 1
    digits = 0
    while value != 0:
        digits += 1
        value = value // 10 
    return digits
def radix_sort(numbers):
    buckets = []
    for i in range(10):
       buckets.append([])
    max_digits = radix_get_max_length(numbers)
    pow_10 = 1
    for digit_index in range(max_digits):
        for num in numbers:
            bucket_index = (num // pow_10) % 10
            buckets[bucket_index].append(num)
        numbers.clear()
        for bucket in buckets:
            numbers.extend(bucket)
            bucket.clear()
      
        pow_10 = pow_10 * 10
   
    negatives = []
    non_negatives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)
        else:
            non_negatives.append(num)
    negatives.reverse()
    numbers.clear()
    numbers.extend(negatives + non_negatives)
numbers = [471, 821, 13313, 325, 3, 916, 351, 264]
print('UNSORTED:', numbers)
radix_sort(numbers)
print('SORTED:', numbers)
