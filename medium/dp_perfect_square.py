
def num_square(n):
    """
    12
    = 4 + minSquare(12 - 4) = 4 + 4 + minSquare(8 - 4)

    https://www.youtube.com/watch?v=KaXeidsmvVQ

    """

    import numpy as np
    dp = np.array([n] * (n+1))

    dp[0] = 0
    dp[1] = 1

    for i in range(1, n+1):
        j = 1
        while j*j <= i:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j += 1

    return dp[n]


print(num_square(8))