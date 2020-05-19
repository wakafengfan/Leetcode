"""

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up(u),down(d),left(l) or right(r),
 but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
 There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.
Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance.
The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included).

Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.

Example 1:
Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller,
because 'l' < 'u'. So the output is "lul".
Example 2:
Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

Output: "impossible"

Explanation: The ball cannot reach the hole.

"""


def maze(maze, start: tuple, dest: tuple):
    m, n = len(maze), len(maze[0])
    q = [(start, 0, [])]
    visited = {start}

    all_step = []

    direction = {'d': (1, 0), 'r': (0, 1), 'u': (-1, 0), 'l': (0, -1)}  # 向右，向下，向左，向上

    while q:
        cur, cur_step, cur_d = q.pop(0)

        # if cur == (0, 2):
        #     print('debug')

        # if cur == dest:
        #     all_step.append((cur_step, cur_d))

        for w, d in direction.items():
            tmp_step = cur_step + 1
            tmp_d = cur_d.copy()
            tmp_d.append(w)

            x = cur[0] + d[0]
            y = cur[1] + d[1]

            if (x, y) == dest:
                all_step.append((tmp_step, tmp_d))

            while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                x += d[0]
                y += d[1]
                tmp_step += 1

                if (x, y) == dest:
                    all_step.append((tmp_step, tmp_d))

            x -= d[0]
            y -= d[1]
            tmp_step -= 1
            if (x, y) not in visited:
                q.append(((x, y), tmp_step, tmp_d))
                visited.add((x, y))

    if not all_step:
        return "impossible"

    all_step = sorted(all_step, key=lambda x: x[0] * 100 + ord(x[1][0]))

    return ''.join(all_step[0][1])


maze1 = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
]

print(maze(maze1, (4,3), (0,1)))
