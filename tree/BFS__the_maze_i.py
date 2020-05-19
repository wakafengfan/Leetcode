"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall.
When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space.
You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.


Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true


Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

"""


def maze(maze, start: tuple, dest: tuple):
    m, n = len(maze), len(maze[0])
    q = [start]
    visited = {start}

    direction = [(1,0), (0,1), (-1,0), (0,-1)]  # 向右，向下，向左，向上

    while q:
        cur = q.pop(0)

        if cur == dest:
            return True

        for d in direction:
            x = cur[0] + d[0]
            y = cur[1] + d[1]

            while 0 < x < m and 0 < y < n and maze[x][y]==0:
                x += d[0]
                y += d[1]
            x -= d[0]
            y -= d[1]
            if (x, y) not in visited:
                q.append((x,y))
                visited.add((x,y))

    return False


the_maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0, 1, 1],[0, 0, 0, 0, 0]]
print(maze(the_maze, (0,4), (4,4)))






