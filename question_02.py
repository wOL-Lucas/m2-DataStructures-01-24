"""
Você foi incumbido de desenvolver um programa para gerenciar uma lista com
extremidades duplas de produtos de mercado. Cada nó da lista representará um produto e
deverá conter as seguintes informações: nome do produto, preço e quantidade em estoque.

As funcionalidades que o programa deve suportar incluem:
• Inserção de um novo produto no início da lista.
• Inserção de um novo produto no final da lista.
• Remoção de um produto específico da lista, com base no nome.
• Busca por um produto na lista, utilizando o nome como critério, e exibição de suas
informações.
• Impressão de todos os produtos presentes na lista, juntamente com suas informações,
em ordem direta e reversa.

"""


class Node:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head

    def isEmpty(self):
        return self.head is None

    def insertFirst(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = node
            return

        previousHead = self.head
        self.head = node
        self.head.next = previousHead
        previousHead.previous = self.head

    def insertLast(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = node
            return

        previousTail = self.tail
        self.tail = node
        self.tail.previous = previousTail
        previousTail.next = self.tail

    def find(self, name: str, display: bool = False):
        current = self.head
        while current is not None:
            if current.name == name:
                if display:
                    print(f"\nName: {current.name}\nPrice: {current.price}")

                return current
            current = current.next
        return None

    def remove(self, name: str):
        if self.isEmpty():
            return

        if self.head.name == name:
            self.head = self.head.next
            self.head.previous = None
            return

        if self.tail.name == name:
            self.tail = self.tail.previous
            self.tail.next = None
            return

        previous = self.head
        current = self.head.next
        while current is not None:
            if current.name == name:
                previous.next = current.next
                current.next.previous = previous
                return
            previous = current
            current = current.next

    def displayAll(self, reverse: bool = False):
        if reverse:
            current = self.tail
            while current is not None:
                print(f"\nName: {current.name}\nPrice: {current.price}")
                current = current.previous
        else:
            current = self.head
            while current is not None:
                print(f"\nName: {current.name}\nPrice: {current.price}")
                current = current.next


if __name__ == "__main__":
    products = [
        Node("Banana", 2.5),
        Node("Apple", 3.5),
        Node("Orange", 4.5),
        Node("Pineapple", 5.5),  # pen pineapple apple pen
    ]

    linkedList = LinkedList(products[0])
    for product in products[1:]:
        linkedList.insertLast(product)

    linkedList.displayAll()

    print("\n\nNow reverse")
    linkedList.displayAll(reverse=True)

    print("\n\nFind")
    linkedList.find("Banana", display=True)

    print("\n\nRemove")
    linkedList.remove("Banana")

    linkedList.displayAll()
