"""

In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.



Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.
​​​​​​​

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.

"""
from heapq import heappush, heappop, heapify





class ExamRoom(object):
    def __init__(self, N):
        self.N = N
        self.pq = []
        heapify(self.pq)
        self.start_map = {}  # 以端点p为左端点的线段
        self.end_map = {}  # 以端点p为右端点的线段
        self.add_interval((-1, N))

    def distance(self, intV):
        x, y = intV
        if x == -1:
            d = y - x
        elif y == self.N:
            d = self.N - x + 1
        else:
            d = (y - x) // 2

        return -d

    def add_interval(self, intV):
        self.start_map[intV[0]] = intV
        self.end_map[intV[1]] = intV
        heappush(self.pq, (self.distance(intV),intV))  # heapq特性，排序会先按端点到区间起点的距离，距离相同的情况再按区间起点的索引

    def remove_interval(self, intV):
        self.start_map.pop(intV[0])
        self.end_map.pop(intV[1])

    def seat(self):
        """
        找最长的线段
        :return:
        """

        # 找最长区间
        _, longest = heappop(self.pq)
        x, y = longest

        # 找位置
        if x == -1:
            p = 0
        elif y == self.N:
            p = self.N-1
        else:
            p = (y-x)//2 + x

        # 添加新区间 （老区间已经被pop 不需要再更新）
        self.add_interval((p, y))
        self.add_interval((x, p))

        return p

    def leave(self, p):
        # 获取端点两边区间
        left = self.end_map[p]
        right = self.start_map[p]

        # 合并两边区间
        self.remove_interval(left)
        self.remove_interval(right)

        self.add_interval((left[0], right[1]))


exam_room = ExamRoom(10)
print(exam_room.seat())
print(exam_room.seat())
print(exam_room.seat())
print(exam_room.seat())
exam_room.leave(4)
print(exam_room.seat())








