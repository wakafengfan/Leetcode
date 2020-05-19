"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

"""



"""
具体的做法是，建立两个堆，这两个堆需要满足:

大顶堆元素都比小顶堆小（由于堆的特点其实只要比较堆顶即可）
大顶堆元素不小于小顶堆，且最多比小顶堆多一个元素
满足上面两个条件的话，如果想要找到中位数，就比较简单了

如果两个堆数量相等（本质是总数为偶数）, 就两个堆顶元素的平均数
如果两个堆数量不相等（本质是总数为奇数）， 就取大顶堆的堆顶元素

"""

from heapq import heappush, heappop

class MedianFinder(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__max_heap = []  # 最大堆实现 是靠取反
        self.__min_heap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # Balance smaller half and larger half.
        if not self.__max_heap or num > -self.__max_heap[0]:  # num比最大堆顶大 则进最小堆
            heappush(self.__min_heap, num)
            if len(self.__min_heap) > len(self.__max_heap) + 1:  # 最小堆个数如果比最大堆多两个及以上 则最小堆吐出来堆顶 放到最大堆
                heappush(self.__max_heap, -heappop(self.__min_heap))
        else:
            heappush(self.__max_heap, -num)  # num比最大堆顶小 （-num比-堆顶大）则放入最大堆
            if len(self.__max_heap) > len(self.__min_heap):  # 最大堆比最小堆多了 则吐出来堆顶到最小堆
                heappush(self.__min_heap, -heappop(self.__max_heap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        # 如果个数同 则堆顶求平均；否则 取小堆顶
        return (-self.__max_heap[0] + self.__min_heap[0]) / 2.0 \
               if len(self.__min_heap) == len(self.__max_heap) \
               else self.__min_heap[0]


if __name__ == '__main__':
    mf = MedianFinder()
    import random
    for i in range(10):
        mf.addNum(random.randint(1,100))
    print(mf.findMedian())