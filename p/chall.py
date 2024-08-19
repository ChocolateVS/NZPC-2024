def minimum_final_score(N, K, A):
    while len(A) >= K:
        min_or = float('inf')
        min_index = -1

        # Find the subarray with the minimum OR value
        for i in range(len(A) - K + 1):
            current_or = 0
            for j in range(K):
                current_or |= A[i + j]
            if current_or < min_or:
                min_or = current_or
                min_index = i
        
        # Replace the selected subarray with the OR value
        A = A[:min_index] + [min_or] + A[min_index + K:]
    
    # Return the sum of the remaining elements
    return sum(A)

# Example usage
N, K = 6, 3
A = [1, 4, 5, 3, 5, 3]
print(minimum_final_score(N, K, A))  # Output should be 8
