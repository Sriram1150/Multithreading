

## Multithreading

 Q1.py – Merge Sort (Single-threaded vs Multi-threaded)

This program compares how fast the Merge Sort algorithm works when run:
- **Normally (single-threaded)**: The program divides the list into smaller pieces and sorts them step-by-step using just one process.
- **With threads (multi-threaded)**: It splits the list into two halves and uses two threads to sort both sides at the same time.

**Steps:**
1. It creates a large list of 10,000 random numbers.
2. It first sorts it using the normal merge sort and records how much time it takes.
3. Then, it sorts a copy of that list using the multi-threaded version.
4. Finally, it prints both times to show which one is faster.

---

 Q2.py – Quicksort (Single-threaded vs Multi-threaded)

This script shows how the Quicksort algorithm can be made faster using threads.

**What it does:**
- It sorts a list of 100,000 random numbers.
- First, it sorts using the regular quicksort method.
- Then, it uses threads to sort different parts of the list at the same time (multi-threaded).
- It compares the time taken by both methods.

**How it works:**
- A pivot is chosen to divide the list into smaller parts.
- The left and right parts are sorted in **separate threads**, which helps speed up the process on computers with multiple cores.

---

 Q3.py – File Downloader (Sequential vs Parallel)

This program downloads multiple files from the internet. It shows how doing downloads **one-by-one** is slower than doing them **all at once using threads**.

**How it works:**
1. It asks the user to:
   - Enter the links manually **or**
   - Load them from a file like `urls.txt`.
2. It downloads all files two ways:
   - **Sequentially**: one after the other.
   - **Parallel (using threads)**: starts multiple downloads at the same time.
3. It creates a folder called `downloads` and saves all files there.
4. It shows how much time each method took.

