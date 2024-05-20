"""

Desenvolva um programa gerenciar uma lista encadeada simples de alunos. Cada nó da lista
representará um aluno e deverá conter as seguintes informações: nome, matrícula e média
do aluno.
O programa deve oferecer suporte às seguintes funcionalidades:
• Inserção de um novo aluno na lista.
• Remoção de um aluno específico da lista, com base na matrícula.
• Busca por um aluno na lista, utilizando a matrícula como critério, e exibição de seus
dados.
• Impressão de todos os alunos presentes na lista, juntamente com suas informações

"""


class Node:
    def __init__(self, name, register, average):
        self.name = name
        self.register = register
        self.average = average
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def isEmpty(self):
        return self.head is None

    def insert(self, node):
        if self.isEmpty():
            self.head = node
            return

        previousHead = self.head
        self.head = node
        self.head.next = previousHead

    def find(self, register: str, display: bool = False):
        current = self.head
        while current is not None:
            if current.register == register:
                if display:
                    print(
                        f"Name: {current.name}\nRegister: {current.register}\nAverage: {current.average}"
                    )

                return current
            current = current.next
        return None

    def remove(self, register: str):
        if self.isEmpty():
            return

        if self.head.register == register:
            self.head = self.head.next
            return

        previous = self.head
        current = self.head.next
        while current is not None:
            if current.register == register:
                previous.next = current.next
                return
            previous = current
            current = current.next

    def displayAll(self):
        current = self.head
        while current is not None:
            print(
                f"Name: {current.name}\nRegister: {current.register}\nAverage: {current.average}\n"
            )
            current = current.next


if __name__ == "__main__":
    students = [
        Node("Maxx", "123", 10),
        Node("John Petrucci", "456", 10),
        Node("Mike Portnoy", "789", 10),
        Node("Jordan Rudess", "101", 10),
        Node("John Myung", "112", 10),
    ]

    linkedList = LinkedList(students[0])
    for student in students[1:]:
        linkedList.insert(student)

    linkedList.displayAll()

    linkedList.find("123", display=True)
    linkedList.remove("123")

    print("\nOnly Dream Theater members now:")
    linkedList.displayAll()
