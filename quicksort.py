"""
Quicksort Algorithm Implementation and Analysis
Author: Shreya Rai

This file contains:
1. Deterministic Quicksort (fixed pivot)
2. Randomized Quicksort (random pivot)
3. Empirical performance testing

To run:
python quicksort.py
"""

import random
import time


# =========================================================
# PART 1: DETERMINISTIC QUICKSORT
# =========================================================

def partition(arr, low, high):
    """
    This function partitions the array around a pivot.

    Steps:
    1. Choose the last element as pivot
    2. Rearrange elements so that:
       - elements <= pivot are on the left
       - elements > pivot are on the right
    3. Place pivot in correct position

    Returns:
        Index of pivot after partition
    """

    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1        # Pointer for smaller element

    # Traverse through all elements
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def deterministic_quicksort(arr, low, high):
    """
    Standard Quicksort implementation using recursion.

    Steps:
    1. Partition the array
    2. Recursively sort left subarray
    3. Recursively sort right subarray
    """

    if low < high:
        # Partition the array
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


# =========================================================
# PART 2: RANDOMIZED QUICKSORT
# =========================================================

def randomized_partition(arr, low, high):
    """
    This function improves pivot selection by choosing a random pivot.

    Steps:
    1. Select a random index between low and high
    2. Swap it with the last element
    3. Use standard partition logic
    """

    random_index = random.randint(low, high)

    # Swap random pivot with last element
    arr[random_index], arr[high] = arr[high], arr[random_index]

    return partition(arr, low, high)


def randomized_quicksort(arr, low, high):
    """
    Randomized Quicksort implementation.

    Advantage:
    Reduces probability of worst-case O(n^2)
    """

    if low < high:
        pi = randomized_partition(arr, low, high)

        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


# =========================================================
# PART 3: EMPIRICAL ANALYSIS
# =========================================================

def generate_datasets(size):
    """
    Generates different types of datasets:
    1. Random data
    2. Sorted data
    3. Reverse sorted data
    """

    random_data = [random.randint(1, 10000) for _ in range(size)]
    sorted_data = sorted(random_data)
    reverse_data = sorted_data[::-1]

    return random_data, sorted_data, reverse_data


def measure_time(sort_function, arr):
    """
    Measures execution time of a sorting function.

    Parameters:
        sort_function: function to execute
        arr: input array

    Returns:
        Execution time in seconds
    """

    start = time.time()

    # Run sorting algorithm
    sort_function(arr, 0, len(arr) - 1)

    end = time.time()

    return end - start


def run_experiment(size):
    """
    Runs performance comparison on different datasets.
    """

    print(f"\n========== Input Size: {size} ==========")

    random_data, sorted_data, reverse_data = generate_datasets(size)

    datasets = {
        "Random": random_data,
        "Sorted": sorted_data,
        "Reverse Sorted": reverse_data
    }

    # Loop through each dataset
    for name, data in datasets.items():
        print(f"\n{name} Data:")

        # Deterministic Quicksort
        arr1 = data.copy()
        time_det = measure_time(deterministic_quicksort, arr1)
        print(f"Deterministic Quicksort Time: {time_det:.6f} seconds")

        # Randomized Quicksort
        arr2 = data.copy()
        time_rand = measure_time(randomized_quicksort, arr2)
        print(f"Randomized Quicksort Time: {time_rand:.6f} seconds")


# =========================================================
# MAIN FUNCTION (IMPORTANT - fixes previous feedback)
# =========================================================

def main():
    """
    Main driver function.

    This function:
    - Defines input sizes
    - Runs experiments
    - Displays results

    This ensures the code is executable and not just function definitions.
    """

    sizes = [100, 500, 1000]

    for size in sizes:
        run_experiment(size)


# Ensures script runs when executed directly
if __name__ == "__main__":
    main()