"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):
    """
    Класс тестирующий класс Stack
    """

    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

    def test_push(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data3')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        data3 = stack.pop()
        data2 = stack.pop()
        data1 = stack.pop()
        data = stack.pop()
        self.assertEqual(data3, "data3")
        self.assertEqual(data2, "data2")
        self.assertEqual(data1, "data1")
        self.assertEqual(data, None)

    def test_stack_str(self):
        stack = Stack()
        self.assertEqual(str(stack), '')
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(str(stack), 'data3\ndata2\ndata1')
