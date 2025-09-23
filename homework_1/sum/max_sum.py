def max_sum_divisible_by_2(arr):
    if not arr:
        return 0
    
    even_numbers = [x for x in arr if x % 2 == 0]
    odd_numbers = [x for x in arr if x % 2 == 1]
    
    even_sum = sum(even_numbers)
    
    if len(odd_numbers) == 0:
        return even_sum
    
    odd_numbers.sort(reverse=True)
    
    if len(odd_numbers) % 2 == 0:
        return even_sum + sum(odd_numbers)
    else:
        return even_sum + sum(odd_numbers[:-1])
