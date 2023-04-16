class MyQueue:

    def __init__(self):
        self.in_stock, self.out_stock = [], []
    
    def push(self, x: int) -> None:
        self.in_stock.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stock.pop()

    def peek(self) -> int:
        if not self.out_stock:
            while self.in_stock:
                self.out_stock.append(self.in_stock.pop())
        return self.out_stock[-1]

    def empty(self) -> bool:
        return not self.in_stock and not self.out_stock
