from typing import List


class Stack(str):
    def __init__(self):
        self.data: List[str] = []

    def push(self, element):
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        is_empty = True
        if self.data:
            is_empty = False
        return is_empty

    def __str__(self) -> str:
        return "[" + ", ".join([f"{self.data[i]}" for i in range(len(self.data) - 1, -1, -1)]) + "]"


