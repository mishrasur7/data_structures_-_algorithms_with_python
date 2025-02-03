class Person:
    def __init__(self, name) -> None:
        self.name = name

    def hello(self) -> str:
        print(f'Hello, my name is {self.name}')