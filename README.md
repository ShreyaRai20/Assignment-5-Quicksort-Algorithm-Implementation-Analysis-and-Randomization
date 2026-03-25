# **Assignment 5 – Quicksort Algorithm: Implementation, Analysis, and Randomization**

## **Author:** Shreya Rai

## **Course:** [MSCS-532-B01]

## **Date:** [March 25,2026]

---

## **Overview**

This repository contains the **deterministic and randomized implementations of the Quicksort algorithm** in Python.

The assignment covers:

- Implementation of standard and randomized Quicksort.
- Analysis of **time complexity** (best, average, worst-case).
- Empirical evaluation on different input distributions: random, sorted, and reverse-sorted.
- Discussion of practical limitations, including recursion depth and memory usage.

---

## **Repository Structure**

```
Assignment5/
│
├── quicksort.py          # Main Quicksort implementation with experiments
├── test_quicksort.py     # Test script to verify correctness
├── README.md             # This file
└── Assignment5_Report.md # Detailed narrative report
```

---

## **Implementation**

### Deterministic Quicksort

- Uses **last element as pivot**.
- Recursively partitions and sorts subarrays.
- Efficient for random inputs, but worst-case occurs on sorted/reverse-sorted arrays.

### Randomized Quicksort

- Pivot is **randomly selected** to prevent worst-case scenarios.
- Performs more consistently across different input distributions.

---

## **How to Run**

### **1. Verify Correctness**

```bash
python3 test_quicksort.py
```

**Expected output:**

```
Original Array: [10, 7, 8, 9, 1, 5]
Sorted (Deterministic): [1, 5, 7, 8, 9, 10]
Sorted (Randomized): [1, 5, 7, 8, 9, 10]
```

### **2. Run Empirical Analysis**

```bash
python3 quicksort.py
```

- Runs experiments on input sizes **100, 500, 1000**.
- Measures **execution time** for deterministic and randomized Quicksort.
- Shows behavior for **random, sorted, and reverse-sorted datasets**.

---

## **Screenshots**

**Add your screenshots in a folder `screenshots/` and link them here:**

- ![Screenshot 1](screenshots/test_quicksort.png) – Correctness verification
- ![Screenshot 2](screenshots/quicksort_times.png) – Timing results
- ![Screenshot 3](screenshots/recursion_error.png) – RecursionError on large sorted input

---

## **Performance Observations**

- Deterministic Quicksort is fast on **random data** but fails for sorted inputs (RecursionError).
- Randomized Quicksort provides **robust performance** across all input types.
- Recursion depth limits deterministic Quicksort on large arrays.
- Randomized pivot selection significantly reduces **likelihood of worst-case O(n²)** behavior.

---

## **References**

- Adinets, A., & Merrill, D. (2022). Onesweep: A faster least-significant-digit radix sort for GPUs. arXiv. [https://doi.org/10.48550/arXiv.2206.01784](https://doi.org/10.48550/arXiv.2206.01784)
- Stehle, E., & Jacobsen, H.-A. (2017). A memory bandwidth-efficient hybrid radix sort on GPUs. Proceedings of the 2017 ACM International Conference on Management of Data, 417–432. [https://doi.org/10.1145/3035918.3064043](https://doi.org/10.1145/3035918.3064043)

---
