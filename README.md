# 🧮 Two Sum Problem (Python)

This Python script solves the classic **Two Sum** problem:  
> Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

---

## 🚀 Problem Description

- You are given an array `nums` and a target integer `target`.
- Return the indices of **two distinct** numbers in the array that sum to the target.
- Assume exactly **one solution exists**, and you **may not use the same element twice**.
- The answer can be returned in any order.

---

## 🧠 Solution Approach

- Uses a **hash map (dictionary)** to store numbers and their indices.
- For each number in the array, check if its complement (`target - num`) exists in the map.
- If yes, return the current index and the index of the complement.
- Runs in **O(n)** time.
