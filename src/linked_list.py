class Node:
    """
    Класс для узла односвязного списка
    """

    def __init__(self, data, next_node=None):
        """
        Инициализатор класса Node
        """

        self.data = data
        self.next_node = next_node


class LinkedList:
    """
    Класс для односвязного списка
    """

    def __init__(self):
        """
        Инициализатор класса LinkedList
        """

        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка
        """

        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next_node = self.head
            self.head = node

    def insert_at_end(self, data: dict) -> None:
        """
        Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка
        """

        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def __str__(self) -> str:
        """
        Вывод данных односвязного списка в строковом представлении
        """
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self):
        """
        Метод возвращающий список с данными LinkedList
        """
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next_node
        return result

    def get_data_by_id(self, value):
        for item in self.to_list():
            try:
                if item['id'] == value:
                    return item
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')

