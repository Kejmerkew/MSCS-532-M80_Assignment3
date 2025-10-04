# README

## Project Overview

This project explores two core algorithmic topics:

1. **Randomized Quicksort vs. Deterministic Quicksort** – We implement and analyze both algorithms to understand their theoretical complexity and practical performance across different input distributions.
2. **Hashing with Chaining** – We implement a hash table that uses chaining for collision resolution, analyze its expected complexity under uniform hashing, and compare theoretical predictions with experimental results.

---

## How to Run the Code

### Requirements

* Python 3.8+
* NumPy (for generating random test data)
* Matplotlib (optional, for plotting results)

Install dependencies if needed:

```bash
pip install numpy matplotlib
```

### Running Quicksort Experiments

Run the script for sorting experiments:

```bash
python Quicksort.py
```

This will:

* Compare **Randomized Quicksort** and **Deterministic Quicksort**.
* Run experiments on arrays of different sizes.
* Test various distributions: random, sorted, reverse-sorted, and arrays with repeated elements.
* Print timing results and scaling checks.

### Running Hashing with Chaining Experiments

Run the script for hash table experiments:

```bash
python HashChaining.py
```

This will:

* Build a hash table with chaining.
* Perform timed **insert**, **search**, and **delete** operations for different load factors.
* Output performance metrics in tabular format.

---

## Summary of Findings

### Randomized Quicksort

* **Theoretical Analysis:** Expected running time is (\Theta(n \log n)), proved via indicator variables and recurrence relations.
* **Empirical Results:**

  * For random data, running time grows proportionally to (n \log n), confirmed by constant ratios (t/(n \ln n)).
  * Randomized Quicksort is **robust**: it avoids (O(n^2)) performance even on sorted or reverse-sorted data, unlike Deterministic Quicksort (first-element pivot).
  * On repeated-element inputs, Randomized Quicksort slows down due to inefficient partitioning, while Deterministic Quicksort sometimes performs better. A 3-way partitioning strategy would improve this.

### Hashing with Chaining

* **Theoretical Analysis:**

  * Insert = (O(1)) expected.
  * Search/Delete = (O(1+\alpha)), where (\alpha = n/m) is the load factor.
* **Empirical Results:**

  * As the load factor increases, performance degrades linearly with (\alpha).
  * With (\alpha = 0.5), operations complete in under 0.001s, but by (\alpha = 5.0), search and delete times increased about 10×.
* **Conclusion:** Maintaining a low load factor (e.g., via dynamic resizing and good hash functions) is critical for constant-time performance.

---
