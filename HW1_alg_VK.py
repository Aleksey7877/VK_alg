import time
import random
import numpy as np
import pytest

# Задача суммы двух чисел
arr_test = [3, 8, 9, 11, 16, 18, 19, 21]
target = 25


def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return nums[left], nums[right], target
        elif sum < target:
            left += 1
        else:
            right -= 1
    return None

# print(twoSum(arr_test, target))


# Задача разворота массива
arr_swope_test = [3, 8, 6, 9, 9, 8, 6]

arr_swope_result = [6, 8, 9, 9, 6, 8, 3]


def swope_array(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    return nums

# print(swope_array(arr_swope_test) == arr_swope_result)


# Задача сдвига массива
arr_turn_test = [1, 2, 3, 4, 5, 6, 7]
k = 3
arr_turn_result = [5, 6, 7, 1, 2, 3, 4]


def turn_array(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


def solution(arr, k):
    arr = turn_array(arr, 0, len(arr) - 1)
    arr = turn_array(arr, 0, k - 1)
    arr = turn_array(arr, k, len(arr) - 1)
    return arr


# print(solution(arr_turn_test, k) == arr_turn_result)

# Задача слияния двух массивов с новым массивом

array_sorted_1 = [3, 8, 10, 11]
array_sorted_2 = [1, 7, 9, 13]
array_result_sorted = [1, 3, 7, 8, 9, 10, 11, 13]


def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    if i < len(arr1):
        merged_array += arr1[i:]
    if j < len(arr2):
        merged_array += arr2[j:]
    return merged_array

# print(merge_sorted_arrays(array_sorted_1, array_sorted_2) == array_result_sorted)

# Задача слияния двух массивов без нового массива


array_sorted_1 = [3, 8, 10, 11]
array_sorted_2 = [1, 7, 9, 13]
array_result_sorted = [1, 3, 7, 8, 9, 10, 11, 13]


def merge_sorted_arrays_2(arr1, arr2):
    pointer1 = len(arr1) - 1  # 3
    pointer2 = len(arr2) - 1  # 3
    pointer3 = len(arr1) + len(arr2) - 1  # 7
    for i in range(len(arr2)):
        arr1.append(0)

    while pointer2 >= 0:
        if pointer1 >= 0 and arr1[pointer1] > arr2[pointer2]:
            arr1[pointer3] = arr1[pointer1]
            pointer1 -= 1
            pointer3 -= 1
        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -= 1
            pointer3 -= 1
    return arr1


arr1 = (merge_sorted_arrays_2(array_sorted_1, array_sorted_2))

# print(arr1 == array_result_sorted)
# print(arr1)

# Задача сортировки массива из 0 и 1
array_10 = [0, 1, 1, 0, 1, 0, 1, 0]


def sort_one(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr


# print(sort_one(array_10))

# Задача сортировки массива из 0, 1 и 2
arr_colors = [2, 0, 2, 1, 1, 0]


def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

# print(sortColors(arr_colors))

# Задача передвижения вперед четных чисел


array_even_test = [3, 2, 4, 1, 11, 8, 9]
array_even_res = [2, 4, 8, 1, 11, 3, 9]


def evenFirst(arr):
    evenIndex = 0
    for i in range(len(arr) - 1):
        if arr[i] % 2 == 0:
            arr[i], arr[evenIndex] = arr[evenIndex], arr[i]
            evenIndex += 1
    return arr

# print(evenFirst(array_even_test) == array_even_res)


# Задача переноса нулей в конец
arr_base1 = [0, 0, 1, 0, 3, 12]
arr_base2 = [0, 33, 57, 88, 60, 0, 0, 80, 99]
arr_base3 = [0, 0, 0, 18, 16, 0, 0, 77, 99]
arr_base4 = [0, 0, 0, 18, 16, 0, 0, 77, 99, 13, 1]

arr_result1 = [1, 3, 12, 0, 0, 0]
arr_result2 = [33, 57, 88, 60, 80, 99, 0, 0, 0]
arr_result3 = [18, 16, 77, 99, 0, 0, 0, 0, 0]
arr_result4 = [18, 16, 77, 99, 13, 1, 0, 0, 0, 0, 0]

# Способ 1


def sort_arr_school(array):
    start_level = 0
    for i in range(len(array)):
        if array[start_level] == 0:
            array.append(array.pop(start_level))
        else:
            start_level += 1
    return array

# Способ 2


def sort_arr_school2(array):
    firstIndex = 0
    lastIndex = len(array) - 1
    while firstIndex <= lastIndex:
        if array[firstIndex] == 0:
            array[firstIndex], array[lastIndex] = array[lastIndex], array[firstIndex]
            lastIndex -= 1
        else:
            firstIndex += 1
    return array


# print(sort_arr_school(arr_base1) == arr_result1)
# print(sort_arr_school(arr_base2) == arr_result2)
# print(sort_arr_school(arr_base3) == arr_result3)
# print(sort_arr_school(arr_base4) == arr_result4)

# print(sort_arr_school2(arr_base1))
# print(sort_arr_school2(arr_base2))
# print(sort_arr_school2(arr_base3))
# print(sort_arr_school2(arr_base4))


def tests():
    # сумма двух чисел
    assert twoSum([3, 8, 9, 11, 16, 18, 19, 21], 25) == (9, 16, 25)

    # разворот массива
    assert swope_array([3, 8, 6, 9, 9, 8, 6]) == [6, 8, 9, 9, 6, 8, 3]

    # сдвиг части массива
    assert solution([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

    # слияние двух массивов (создание третьего нового)
    assert merge_sorted_arrays([3, 8, 10, 11], [1, 7, 9, 13]) == [
        1, 3, 7, 8, 9, 10, 11, 13]

    # слияние двух массивов без создания третьего
    assert merge_sorted_arrays_2([3, 8, 10, 11], [1, 7, 9, 13]) == [
        1, 3, 7, 8, 9, 10, 11, 13]

    # сортировка массива из 0 и 1
    assert sort_one([0, 1, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]

    # сортировка массива из 0, 1 и 2
    assert sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]

    # предвижение вперед четных чисел
    assert evenFirst([3, 2, 4, 1, 11, 8, 9]) == [2, 4, 8, 1, 11, 3, 9]


def test_sort_arr_school():
    # Тест варианта 1
    assert sort_arr_school([0, 0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0, 0]
    assert sort_arr_school([0, 33, 57, 88, 60, 0, 0, 80, 99]) == [
        33, 57, 88, 60, 80, 99, 0, 0, 0]
    assert sort_arr_school([0, 0, 0, 18, 16, 0, 0, 77, 99]) == [
        18, 16, 77, 99, 0, 0, 0, 0, 0]
    assert sort_arr_school([0, 0, 0, 18, 16, 0, 0, 77, 99, 13, 1]) == [
        18, 16, 77, 99, 13, 1, 0, 0, 0, 0, 0]

    # Тест варианта 2
    assert sort_arr_school2([0, 0, 1, 0, 3, 12]) == [12, 3, 1, 0, 0, 0]
    assert sort_arr_school2([0, 33, 57, 88, 60, 0, 0, 80, 99]) == [
        99, 33, 57, 88, 60, 80, 0, 0, 0]
    assert sort_arr_school2([0, 0, 0, 18, 16, 0, 0, 77, 99]) == [
        99, 77, 16, 18, 0, 0, 0, 0, 0]
    assert sort_arr_school2([0, 0, 0, 18, 16, 0, 0, 77, 99, 13, 1]) == [
        1, 13, 99, 18, 16, 77, 0, 0, 0, 0, 0]


def test_sort_arr_school2():
    # Тест на обычный случай
    assert sort_arr_school2([1, 0, 1, 0, 1]) == [1, 1, 1, 0, 0]
    # Тест на пустой массив
    assert sort_arr_school2([]) == []
    # Тест на массив, содержащий только единицы
    assert sort_arr_school2([1, 1, 1]) == [1, 1, 1]
    # Тест на массив, содержащий только нули
    assert sort_arr_school2([0, 0, 0]) == [0, 0, 0]
    # Тест на уже отсортированный массив
    assert sort_arr_school2([1, 1, 0, 0]) == [1, 1, 0, 0]
    # Тест на массив из одного элемента
    assert sort_arr_school2([1]) == [1]
    assert sort_arr_school2([0]) == [0]
    # Тест на случай, когда все 0 должны быть перемещены в конец
    assert sort_arr_school2([0, 1, 0, 1, 1, 0]) == [1, 1, 1, 0, 0, 0]
