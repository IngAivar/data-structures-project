class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = self.tail = None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = ''
        if self.head is None:
            return result
        index = self.head
        while index:
            result += index.data + chr(10)
            index = index.next_node
        return result[:-1]

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь
        :param data: данные, которые будут добавлены в очередь
        """
        if self.head is None:  # пустая очередь
            self.head = Node(data, None)  # создаем голову
        else:  # непустая очередь
            if self.tail is None:  # 2 элемента в очереди
                self.tail = Node(data, None)
                self.head.next_node = self.tail  # голова ссылается на хвост
            else:  # 3 и более элементов в очереди
                tail = self.tail  # сохраняем текущий хвост
                self.tail = Node(data, None)  # наращиваем хвост
                tail.next_node = self.tail  # предыдущий хвост ссылается на новый

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        :return: данные удаленного элемента
        """
        if self.head is None and self.tail is None:
            return None
        if self.head is not None:
            pop_q = self.head
            if self.head.data == self.tail.data:
                self.tail = None
            self.head = self.head.next_node
            return pop_q.data
