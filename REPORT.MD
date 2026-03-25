# **Assignment 5 Report: Quicksort Algorithm – Implementation, Analysis, and Randomization**

## **Student Name:** Shreya Rai

## **Course:** [MSCS-532-B01]

## **Date:** [March 25,2026]

---

## **1. Overview**

This assignment focuses on the **Quicksort algorithm**, both deterministic and randomized versions, including implementation, theoretical analysis, and empirical testing. The objectives were:

1. Implement **deterministic and randomized Quicksort** in Python.
2. Analyze **time and space complexities** in best, average, and worst cases.
3. Compare performance across **different input distributions** (random, sorted, reverse-sorted).
4. Understand practical limitations and benefits of randomization in Quicksort.

The assignment demonstrates how algorithm design decisions impact **efficiency and scalability** in software systems.

---

## **2. Implementation Narrative**

### **Deterministic Quicksort**

- Pivot is chosen as the **last element** of the subarray.
- Partitioning rearranges elements such that all elements ≤ pivot are on the left, and > pivot on the right.
- Recursive calls sort the left and right subarrays until the entire array is sorted.
- Efficient on random or average data, but can degrade to **O(n²)** for sorted or reverse-sorted arrays.

### **Randomized Quicksort**

- Pivot is chosen **randomly** from the subarray.
- Partitioning logic is identical to deterministic version.
- Reduces likelihood of worst-case performance by ensuring pivot selection is unpredictable.

### **Execution Process**

- Added a **main driver** to run the algorithms on multiple input sizes.
- Generated **random, sorted, and reverse-sorted arrays**.
- Measured **execution time** for deterministic and randomized Quicksort.
- Extensive **inline comments** added for clarity, addressing previous feedback.

---

## **3. Theoretical Analysis**

| Case             | Deterministic QS | Randomized QS       |
| ---------------- | ---------------- | ------------------- |
| Best-case        | O(n log n)       | O(n log n)          |
| Average-case     | O(n log n)       | O(n log n)          |
| Worst-case       | O(n²)            | O(n log n) expected |
| Space Complexity | O(log n) stack   | O(log n) stack      |

**Observations:**

- Deterministic Quicksort has **O(n²)** worst-case for sorted inputs due to poor pivot selection.
- Randomized Quicksort reduces probability of encountering worst-case, providing more **robust performance**.
- Both use recursive stack space and are considered **in-place algorithms**.

---

## **4. Empirical Analysis**

### **Method**

- Input sizes: 100, 500, 1000 elements.
- Dataset types: **Random**, **Sorted**, **Reverse-Sorted**.
- Measured execution time in seconds for both deterministic and randomized Quicksort.

### **Results**

**Placeholder for Screenshots:**

1. Screenshot of `test_quicksort.py` output – showing correctness.
2. Screenshot of `quicksort.py` output – showing timing results.
3. Screenshot of RecursionError for deterministic Quicksort on larger sorted input.

**Sample Observations from Experiment:**

| Input Type     | Deterministic QS Time (s) | Randomized QS Time (s) |
| -------------- | ------------------------- | ---------------------- |
| Random (1000)  | 0.000698                  | 0.000937               |
| Sorted (1000)  | **RecursionError**        | 0.00105                |
| Reverse (1000) | 0.005752                  | 0.000613               |

**Insights:**

- Deterministic Quicksort fails on **large sorted inputs** due to recursion depth, confirming **theoretical worst-case**.
- Randomized Quicksort performs consistently across all distributions.
- Random pivot selection is highly recommended for general-purpose sorting.

---

## **5. Discussion**

- **Deterministic Quicksort:** Fast for random data but highly sensitive to input order.
- **Randomized Quicksort:** Avoids worst-case scenarios; better for unknown or large datasets.
- **Memory Usage:** Both algorithms are in-place but recursion depth can affect stack memory.
- **Practical Implication:** Randomized Quicksort is more suitable for **real-world applications** where input distribution is unknown.

---

## **6. Conclusion**

- Quicksort remains a **high-performance sorting algorithm** with average-case efficiency of **O(n log n)**.
- Randomized Quicksort offers **robust performance**, reducing the risk of worst-case behavior.
- Deterministic Quicksort can be used when input distribution is predictable but is **risky for sorted or reverse-sorted data**.
- The assignment emphasizes the importance of **algorithm selection** and understanding input characteristics in software engineering.

---

## **7. Screenshots**

**[Insert your screenshots here]**

- Screenshot 1: Correctness verification (`test_quicksort.py`)

- Screenshot 2: Timing analysis (`quicksort.py`)

- Screenshot 3: RecursionError for large sorted input

---

## **8. References**

- Adinets, A., & Merrill, D. (2022). Onesweep: A faster least-significant-digit radix sort for GPUs. arXiv. [https://doi.org/10.48550/arXiv.2206.01784](https://doi.org/10.48550/arXiv.2206.01784)
- Stehle, E., & Jacobsen, H.-A. (2017). A memory bandwidth-efficient hybrid radix sort on GPUs. Proceedings of the 2017 ACM International Conference on Management of Data, 417–432. [https://doi.org/10.1145/3035918.3064043](https://doi.org/10.1145/3035918.3064043)

---
