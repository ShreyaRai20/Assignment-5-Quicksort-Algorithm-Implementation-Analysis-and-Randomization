"""
Simple test file to verify correctness of Quicksort implementations
"""

from quicksort import deterministic_quicksort, randomized_quicksort

# Test array
arr = [10, 7, 8, 9, 1, 5]

print("Original Array:", arr)

# Deterministic
arr1 = arr.copy()
deterministic_quicksort(arr1, 0, len(arr1) - 1)
print("Sorted (Deterministic):", arr1)

# Randomized
arr2 = arr.copy()
randomized_quicksort(arr2, 0, len(arr2) - 1)
print("Sorted (Randomized):", arr2)