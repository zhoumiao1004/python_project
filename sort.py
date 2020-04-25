# -*- coding:utf-8 -*-
import random


class Solution:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def bubble_sort(self):
        data = self.data[:]
        n = len(data)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    def select_sort(self):
        data = self.data[:]
        n = len(data)
        for i in range(n):
            min_index = i
            for j in range(i, n):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data

    @staticmethod
    def _partition(data, left, right):
        pivot = data[left]
        while left < right:
            while left < right and data[right] >= pivot:
                right -= 1
            data[left] = data[right]
            while left < right and data[left] <= pivot:
                left += 1
            data[right] = data[left]
        data[left] = pivot
        return left

    @staticmethod
    def _partition2(arr, low, high):
        pivot = arr[high]
        index = low
        for i in range(low, high):
            if arr[i] < pivot:
                arr[i], arr[index] = arr[index], arr[i]
                index += 1
        arr[index], arr[high] = arr[high], arr[index]

        return index

    def quick(self, data, left, right):
        if left < right:
            mid = self._partition(data, left, right)
            self.quick(data, left, mid - 1)
            self.quick(data, mid + 1, right)

    def quick_sort(self):
        data = self.data[:]
        self.quick(data, 0, len(data) - 1)
        return data

    def insert_sort(self):
        data = self.data[:]
        n = len(data)
        for i in range(1, n):
            tmp = data[i]  # 需要站队的数
            for j in range(i, -1, -1):
                if tmp < data[j - 1]:
                    data[j] = data[j - 1]  # 前面的数往后站
                else:
                    break
            data[j] = tmp

        return data

    def merge_sort(self):
        data = self.data[:]
        return self._merge_sort(data)

    def _merge_sort(self, data):
        if len(data) <= 1:
            return data
        pivot_index = len(data) / 2
        left = self._merge_sort(data[:pivot_index])
        right = self._merge_sort(data[pivot_index:])
        return self._merge(left, right)

    @staticmethod
    def _merge(left, right):
        l, r = 0, 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        result += left[l:]
        result += right[r:]
        return result


int_array = [random.randint(1, 100) for i in range(10)]
print('orgin data is: {}'.format(int_array))
s = Solution(int_array)
print('bubble sort begin.')
print s.bubble_sort()
print('select sort begin.')
print s.select_sort()
print('quick sort begin.')
print s.quick_sort()
print('insert sort begin.')
print s.insert_sort()
print('merge sort begin.')
print s.merge_sort()
