"""
小兔的叔叔从外面旅游回来给她带来了一个礼物，小兔高兴地跑回自己的房间，拆开一看是一个棋盘，小兔有所失望。不
 过没过几天发现了棋盘的好玩之处。从起点(0，0)走到终点(n,n)的最短路径数是C(2n,n),现在小兔又想如果不穿越对角线(但可接触对角线上的格点)，
 这样的路径数有多少?小兔想了很长时间都没想出来，现在想请你帮助小兔解决这个问题，对于你来说应该不难吧!
Input
每次输入一个数n(1<=n<=35)，当n等于－1时结束输入。
Output
对于每个输入数据输出路径数，具体格式看Sample。
Sample Input
1
3
12
-1
Sample Output
1 1 2
2 3 10
3 12 416024


"""

import numpy as np


def chess():
    a = np.array([[0]*40]*40)  # 到达（i，j）需要的路径数

    for i in range(1, 37):
        a[0][i] = 1

    for i in range(1, 37):  # row
        for j in range(i, 37):  # col
            if i == j:
                a[i][j] = a[i-1][j]  # 如遇对角线，和上边相同
            else:
                a[i][j] = a[i-1][j] + a[i][j-1]

    return a

n = 0
while n != -1:

    n = input("请输入")
    n = int(n)
    a_= chess()

    print(a_[n][n] *2)





