# Two_egg_problem

Solve two egg problem in python.

## Problem description

***Problem Statement***

You are faced with a building of 100 floors and given 2 eggs.
It is known that there is a critical floor in this building, such that if an egg is dropped from this floor, it will not break.
The question is: In the worst-case scenario, how many times do you need to drop eggs to determine this critical floor?

***Analysis***

Let the number of eggs be denoted as N, and the number of drops be denoted as M.

If N = 1, then M = 100.

If N approaches infinity, we can use binary search, where 2<sup>M</sup> >= 100, yielding M = 7.

Now, let's consider the case when N = 2. The first egg A should be used to determine the range of possible critical floors, while the second egg B is used to test each floor individually.

We must also ensure that as egg A's drops increase, egg B's drops decrease, so that the total number of drops is minimized.

Assuming egg A is dropped at intervals of n, then the second drop is at n-1, and so on.

n + (n-1) + (n-2) + ... + 1 >= 100

The smallest possible value for n is found to be 14.

The floors where egg A is dropped are 14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, 100.

Hence, the final answer is M = 14.

***Generalization***

Let there be T floors, N eggs, and at most M attempts to find the critical floor. We seek to find M(T,N).

| T\N |  1  |  2  |  3  |  4  |
| :-: | :-: | :-: | :-: | :-: |
|  1  |  1  |  1  |  1  |  1  |
|  2  |  2  |  M(2,2)  |  M(2,3)  |  M(2,4)  |
|  3  |  3  |  M(3,2)  |  M(3,3)  |  M(3,4)  |

Assume the first egg is dropped from floor k. If it breaks, the remaining attempts are M(k,N-1), and if it doesn't break, the remaining attempts are M(T-k,N).

Hence, for this case, M<sub>k</sub>(T,N) = max{M(k,N-1),M(T-k,N)} + 1.

Since k can take any value from 1 to T, we need to find the optimal solution, so M(T,N) = min{M<sub>1</sub>,M<sub>2</sub>,...,M<sub>T</sub>}.

Thus, we can recursively compute the values of M(T,N).
