from math import log2, ceil


def egg_drop(t: int, n: int) -> int:
    memo = {}

    def drops(t: int, n: int) -> int:
        # base case
        if n == 1:
            return t
        if t == 1 or t == 2:
            return 1
        if t == 0:
            return 0
        if n >= t:
            return ceil(log2(t))

        # avoid repeated calculation
        if (t, n) in memo:
            return memo[(t, n)]

        # # linear search
        # res = float('INF')
        # for k in range(1, t + 1):
        #     res = min(res, max(drops(k - 1, n - 1), drops(t - k, n)) + 1)

        # binary search, find the valley point
        res = float('INF')
        lo, hi = 1, t
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = drops(mid - 1, n - 1)
            not_broken = drops(t - mid, n)
            if broken < not_broken:
                lo = mid + 1
                res = min(res, not_broken + 1)
            else:
                hi = mid - 1
                res = min(res, broken + 1)

        memo[(t, n)] = res  # Store the minimum drop count in memo

        return res

    return drops(t, n)


if __name__ == "__main__":
    floor_num = int(input('Floor number:'))
    egg_num = int(input('Egg number:'))
    print(f'At least {egg_drop(floor_num, egg_num)} drops are needed.')
