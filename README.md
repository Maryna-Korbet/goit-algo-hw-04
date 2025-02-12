# Sorting Algorithm Performance Analysis

## Task Description
Python has two built-in sorting functions: `sorted` and `sort`. These functions use **Timsort**, a hybrid sorting algorithm that combines **Merge Sort** and **Insertion Sort**.

In this analysis, we compare three sorting algorithms: **Merge Sort**, **Insertion Sort**, and **Timsort** based on execution time. The performance of these algorithms is tested on different array sizes to empirically validate their theoretical time complexity. The `timeit` module is used for measuring execution time.

## Introduction

This analysis compares three sorting algorithms: **Merge Sort**, **Insertion Sort**, and **Timsort** (Python's built-in `sorted` function). The performance of these algorithms is measured on different array sizes to empirically validate their time complexity.

## Test Results

### Array Size: 100

- **Merge Sort**: 0.000150 seconds
- **Insertion Sort**: 0.000189 seconds
- **Timsort (Python's sorted)**: 0.000011 seconds

### Array Size: 1000

- **Merge Sort**: 0.001942 seconds
- **Insertion Sort**: 0.022763 seconds
- **Timsort (Python's sorted)**: 0.000106 seconds

### Array Size: 5000

- **Merge Sort**: 0.012758 seconds
- **Insertion Sort**: 0.601573 seconds
- **Timsort (Python's sorted)**: 0.000553 seconds

### Array Size: 10000

- **Merge Sort**: 0.023918 seconds
- **Insertion Sort**: 2.495128 seconds
- **Timsort (Python's sorted)**: 0.001229 seconds

## Conclusions

1. **Insertion Sort** is significantly slower on large datasets due to its **O(n²)** time complexity. While it performs well for small arrays, it becomes inefficient as the array size increases.
2. **Merge Sort** consistently performs well with an **O(n log n)** time complexity. However, it is outperformed by Timsort due to additional optimizations.
3. **Timsort** (Python's `sorted` function) is the fastest algorithm across all tested cases. It efficiently combines **Merge Sort** and **Insertion Sort**, adapting to the data distribution to provide optimal performance.
4. The results confirm that **Timsort's hybrid approach** makes it superior for real-world applications, which is why it is the default sorting algorithm in Python.

## Key Takeaway

For practical applications, **Timsort** is the best choice due to its **speed and adaptability**, while **Merge Sort** remains a strong alternative for predictable performance. **Insertion Sort** should be used only for very small datasets.
