"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = Node({'id': 1}, None)

    def test_node_init(self):
        self.assertEqual(self.node.data, {'id': 1})
        self.assertEqual(self.node.next_node, None)


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.LinkedList = LinkedList()

    def test_LinkedList_init(self):
        self.assertEqual(self.LinkedList.tail, None)
        self.assertEqual(self.LinkedList.head, None)

    def test_enLinkedList_str_insert_beginning_insert_at_end(self):
        self.LinkedList.insert_beginning({'id': 1})
        self.assertEqual(self.LinkedList.head.data, {'id': 1})
        self.LinkedList.insert_at_end({'id': 2})
        self.assertEqual(self.LinkedList.tail.data, {'id': 2})
        self.LinkedList.insert_at_end({'id': 3})
        self.assertEqual(self.LinkedList.tail.data, {'id': 3})
        self.LinkedList.insert_beginning({'id': 0})
        self.assertEqual(self.LinkedList.head.data, {'id': 0})
        assert str(self.LinkedList) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"

    def test_to_list(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({2: 2})
        linked_list.insert_beginning({1: 1})
        linked_list.insert_at_end({3: 3})
        linked_list.insert_at_end({4: 4})
        self.assertEqual(linked_list.to_list(), [{1: 1}, {2: 2}, {3: 3}, {4: 4}])

    def test_get_data_by_id(self):
        linked_list = LinkedList()
        linked_list.insert_beginning([1, 1])
        self.assertEqual(linked_list.get_data_by_id(1), None)
        linked_list.insert_beginning({'id': 2})
        self.assertEqual(linked_list.get_data_by_id(2), {'id': 2})
