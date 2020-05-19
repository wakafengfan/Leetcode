"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination.
The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).
If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

"""


def maze(maze, start: tuple, dest: tuple):
    m, n = len(maze), len(maze[0])
    q = [(start, 0)]
    visited = {start}

    all_step = []

    direction = [(1,0), (0,1), (-1,0), (0,-1)]  # 向右，向下，向左，向上

    while q:
        cur, cur_step = q.pop(0)

        if cur == dest:
            all_step.append(cur_step)

        for d in direction:
            tmp_step = cur_step + 1
            x = cur[0] + d[0]
            y = cur[1] + d[1]

            while 0 < x < m and 0 < y < n and maze[x][y]==0:
                x += d[0]
                y += d[1]
                tmp_step += 1

            x -= d[0]
            y -= d[1]
            tmp_step -= 1

            if (x, y) not in visited:
                q.append(((x,y), tmp_step))
                visited.add((x,y))

    return min(all_step) if all_step else -1


the_maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0, 1, 1],[0, 0, 0, 0, 0]]
print(maze(the_maze, (0,4), (4,4)))
print(maze(the_maze, (0,4), (3,2)))






