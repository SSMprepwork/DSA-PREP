# Understanding Greedy Algorithms

Greedy algorithms are a powerful and efficient problem-solving method that follows the principle of making the **locally optimal choice** at each step in hopes of finding a global optimum. This approach builds up a solution incrementally, always choosing the best option available at the moment. Let’s dive into a detailed explanation with examples and discuss their time complexity, space complexity, and the data structures they use.

## 1. What is a Greedy Algorithm?

A greedy algorithm solves problems by taking the best possible solution at each small step. It doesn’t look ahead to see the entire problem space; it just focuses on immediate benefits. This simple, step-by-step approach works well for many optimization problems, but it doesn’t guarantee the optimal solution for every problem.

### Example 1: Navigation (Shortest Route Problem)

When you use a navigation app like Google Maps, the algorithm aims to find the shortest or fastest route from your starting point to your destination. It evaluates each possible path segment based on factors such as distance or traffic conditions and selects the shortest or least congested path at each intersection. As conditions change, the app updates and makes the best decision for the next segment, optimizing your route in real-time.

This approach is a classic application of a greedy algorithm, as the app makes a locally optimal choice at each point, seeking to minimize travel time. However, this method may not always be perfect since it might not account for future traffic changes or road closures.

### Example 2: Activity Selection Problem

In this problem, the goal is to select the maximum number of non-overlapping activities from a list. The greedy algorithm sorts the activities by their finishing times and picks the one that ends the earliest, ensuring maximum room for subsequent activities.

## 2. Time Complexity, Space Complexity, and Data Structures Used

### a) Navigation (Shortest Route Problem)
- **Time Complexity**: O(E log V), where E is the number of roads (edges) and V is the number of locations (vertices). Algorithms like Dijkstra's may be used, which perform efficiently with a priority queue.
- **Space Complexity**: O(V), where V is the number of locations. This is used for storing distances and paths.
- **Data Structure**: A priority queue (min-heap) is typically used to select the next shortest path quickly, and a graph structure represents the map’s nodes and edges.

### b) Coin Change Problem
- **Time Complexity**: O(N), where N is the amount to be changed. In each step, the algorithm performs a division operation to find how many coins of a particular denomination fit into the remaining amount.
- **Space Complexity**: O(1), as it uses a constant amount of space for variables.
- **Data Structure**: The algorithm often uses a list or array to hold the denominations of the coins. No complex data structures are needed.

### c) Activity Selection Problem
- **Time Complexity**: O(N log N), where N is the number of activities. This complexity arises from sorting the activities based on their end times.
- **Space Complexity**: O(1) if we sort in place, but can be O(N) if a new array is used for sorting.
- **Data Structure**: An array or list is typically used to store the activities and their start and end times.

### d) Kruskal's Algorithm (for Minimum Spanning Tree)
- **Time Complexity**: O(E log E), where E is the number of edges. This is because the algorithm sorts the edges by weight and uses union-find operations.
- **Space Complexity**: O(V), where V is the number of vertices. It uses space to store the parent and rank arrays for union-find.
- **Data Structure**: This algorithm uses the Union-Find (Disjoint Set Union, DSU) data structure to efficiently detect and merge cycles while building the MST.

### e) Fractional Knapsack Problem
- **Time Complexity**: O(N log N), where N is the number of items. The algorithm sorts the items based on the ratio of value to weight.
- **Space Complexity**: O(1) if sorted in place, otherwise O(N).
- **Data Structure**: An array or list is used to store item weights and values, and the ratio is calculated during sorting.

### Summary Table

| Algorithm                   | Time Complexity | Space Complexity | Data Structure Used      |
|----------------------------|-----------------|------------------|--------------------------|
| Navigation (Shortest Route) | O(E log V)      | O(V)             | Priority Queue, Graph    |
| Coin Change Problem        | O(N)            | O(1)             | Array/List               |
| Activity Selection Problem | O(N log N)      | O(1) or O(N)     | Array/List               |
| Kruskal's Algorithm        | O(E log E)      | O(V)             | Union-Find (DSU)         |
| Fractional Knapsack        | O(N log N)      | O(1) or O(N)     | Array/List               |

## Conclusion

Greedy algorithms are efficient and easy to implement, but they are not always optimal. Their performance depends heavily on the nature of the problem and the properties like **optimal substructure** and **greedy choice property**. Understanding the time and space complexity helps evaluate when and where a greedy approach is suitable.



# Understanding Dynamic Programming (DP)

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into smaller subproblems, solving each subproblem once, and storing its solution. DP is used when a problem has **overlapping subproblems** and **optimal substructure**, meaning that a complex problem can be composed of smaller, simpler problems that share components.

DP solutions are typically more efficient than naive recursive solutions because they avoid redundant calculations by **memoizing** or **tabulating** results.

## 1. What is Dynamic Programming?

Dynamic programming is an approach where a problem is broken down into smaller, overlapping subproblems, and their results are stored to avoid recalculating them. There are two main techniques:
- **Top-Down (Memoization)**: Solves the problem using a recursive approach, storing results as they are computed.
- **Bottom-Up (Tabulation)**: Builds up solutions iteratively, starting from the smallest subproblem and working up to the main problem.

### Example 1: Fibonacci Sequence (Memoization)

In a naive recursive approach, calculating the Fibonacci number `F(n)` involves recalculating `F(n-1)` and `F(n-2)` multiple times. In DP, you store these values once calculated, avoiding redundant work.

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

### Example 2: Knapsack Problem (Tabulation)

In the **0/1 Knapsack Problem**, you have items with weights and values and a knapsack with a maximum capacity. You must choose items to maximize the total value without exceeding the capacity. A DP table is used to store the maximum value achievable with different capacities and items, avoiding the need to recompute combinations.

```python
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

### Example 3: Optimal Route Planning in Daily Life (Dynamic Route Planning)

Modern navigation apps use a dynamic programming approach to find not only the shortest route but also alternate routes, considering future traffic patterns. The algorithm dynamically updates and stores path information, adjusting as conditions change. Unlike the greedy approach, which chooses the shortest segment at each step, DP considers future intersections and combines results to find an overall optimal route.

## 2. Time Complexity, Space Complexity, and Data Structures Used

### a) Fibonacci Sequence (Memoization)
- **Time Complexity**: O(N), where N is the number to find in the sequence. By storing previous results, each call is made only once.
- **Space Complexity**: O(N) due to the storage of memoized results.
- **Data Structure**: A dictionary or array is used to store the computed Fibonacci values.

### b) 0/1 Knapsack Problem (Tabulation)
- **Time Complexity**: O(N * W), where N is the number of items and W is the capacity of the knapsack.
- **Space Complexity**: O(N * W) due to the DP table used to store intermediate results.
- **Data Structure**: A 2D array (table) is used to store the maximum value for each item and capacity combination.

### c) Longest Common Subsequence (LCS) Problem
- **Time Complexity**: O(N * M), where N and M are the lengths of the two sequences being compared.
- **Space Complexity**: O(N * M) due to the DP table used to store solutions to subproblems.
- **Data Structure**: A 2D array (table) is used to store the lengths of the longest common subsequences for different substrings.

### d) Optimal Route Planning
- **Time Complexity**: O(V^2) for algorithms like Floyd-Warshall that find shortest paths between all pairs of vertices (where V is the number of locations).
- **Space Complexity**: O(V^2) due to storing the paths and distances between all pairs of locations.
- **Data Structure**: A 2D array (graph matrix) is used to store distances, and another for tracking paths.

### Summary Table

| Algorithm                   | Time Complexity | Space Complexity | Data Structure Used      |
|----------------------------|-----------------|------------------|--------------------------|
| Fibonacci (Memoization)    | O(N)            | O(N)             | Dictionary/Array         |
| 0/1 Knapsack Problem       | O(N * W)        | O(N * W)         | 2D Array (Table)         |
| Longest Common Subsequence | O(N * M)        | O(N * M)         | 2D Array (Table)         |
| Optimal Route Planning     | O(V^2)          | O(V^2)           | 2D Array (Graph Matrix)  |

## Conclusion

Dynamic Programming is a highly efficient technique for solving optimization problems when overlapping subproblems and optimal substructure are present. By storing intermediate results, DP reduces the need for repetitive computations, offering significant performance improvements over naive approaches. Understanding time and space complexity, along with suitable data structures, helps in designing and applying DP solutions effectively.

