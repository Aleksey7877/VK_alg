import time
import numpy as np
import pytest
from collections import deque
from queue import Queue


class ListNode:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"{self.value}"


class Cycle_list:
    def hasCycle(head):
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


class Reverse_list:
    def reverseLinkedList(head):
        prev = None
        current = head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        head = prev
        return head


class Middle:
    def middleNode(head):
        slow = head
        fast = head

        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow


class Remove:
    def removeElements(head, value):
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head

        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return dummy.next


class Sub:
    def isSubsequence(a, b):

        q = Queue()

        while a is not None:
            q.put(a.value)
            a = a.next

        while b is not None and not q.empty():
            if q.queue[0] == b.value:
                q.get()
            b = b.next

        return q.empty()


def is_palindrome(s):
    stack = []
    for char in s:
        stack.append(char)
    for char in s:
        if char != stack.pop():
            return False
    return True


def is_palindrome2(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def tests():

    # Создаем список с 1 по 6 и связываем
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    # проверка на наличие циклов в списке
    assert Cycle_list.hasCycle(node1) == False

    # добавили цикл с 6 на 3
    node6.next = node3
    assert Cycle_list.hasCycle(node1) == True

    # Убираем цикл
    node6.next = None

    # Тестируем разворот списка в обратном порядке
    # Перевернули туда-обратно
    assert Reverse_list.reverseLinkedList(node1) == node6
    assert Reverse_list.reverseLinkedList(node6) == node1

    # Находим середину
    assert Middle.middleNode(node1) == node4

    # Проверяем, что при удалении "2" после 1 будет идти 3
    assert (Remove.removeElements(node1, 2).value,
            Remove.removeElements(node1, 2).next.value) == (1, 3)

    # Проверим, содержится ли "подмассив" в исходном массиве
    example_node0 = ListNode(1)
    example_node1 = ListNode(3)
    example_node2 = ListNode(4)
    example_node3 = ListNode(5)
    example_node1.next = example_node2
    example_node2.next = example_node3

    assert Sub.isSubsequence(example_node0, node1) == True

    # Проверим, что он не является дочерним, если мы возьмем начальный элемент как 3
    assert Sub.isSubsequence(example_node0, node3) == False

    # Проверяем на палиндром 1 вариант
    assert is_palindrome("шалаш") == True
    assert is_palindrome("гамак") == False

    # 2 вариант
    assert is_palindrome2("шалаш") == True
    assert is_palindrome2("гамак") == False
    assert is_palindrome2("ы") == True
    assert is_palindrome2("") == True
