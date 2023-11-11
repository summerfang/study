def maximumProductSum(memory):
    n = len(memory)
    mod = 10**9 + 7
    
    # Initialize variables to store the maximum efficiency and total sum
    max_efficiency = 0
    total_sum = sum(memory)
    
    # Iterate through possible values of idx
    for idx in range(2, n // 2 + 1):
        # Calculate efficiency for this idx
        efficiency = idx * (total_sum - memory[idx - 1] - memory[n - idx])
        max_efficiency = max(max_efficiency, efficiency)
    
    return max_efficiency % mod

# Example usage:
n = 5
memory = [1, 2, 3, 4, 5]
result = maximumProductSum(memory)
print(result)  # This will print the