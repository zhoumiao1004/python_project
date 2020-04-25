# coding:utf-8

import heapq


class TopKHeap:
    # 保存最大k个数的堆
    def __init__(self, k):
        self.k = k
        self.data = []

    def push(self, elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            # 只要比最小的数大就加进来
            smallest = self.data[0]
            if elem > smallest:
                heapq.heapreplace(self.data, elem)

    def topk(self):
        return [x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])]


class BtmKHeap:
    # 保存最小k个数的堆
    def __init__(self, k):
        self.k = k
        self.data = []

    def push(self, elem):
        elem = -elem
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            # 只要比最小的数大就加进来
            smallest = self.data[0]
            if elem > smallest:
                heapq.heapreplace(self.data, elem)

    def topk(self):
        return [-x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    th = TopKHeap(5)
    for i in arr:
        th.push(i)

    print th.topk()

    bh = BtmKHeap(5)
    for i in arr:
        bh.push(i)

    print bh.topk()
