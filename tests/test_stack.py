"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest
from src.stack import Stack


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
