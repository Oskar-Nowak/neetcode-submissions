class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_val = val
        elif val >= self.min_val:
            self.stack.append(val) # Normalna wartość
        else:
            # Wrzucamy "zakodowany" ślad. 
            # Ponieważ val < min_val, to (2 * val - min_val) będzie ZAWSZE mniejsze od val!
            encoded_val = 2 * val - self.min_val
            self.stack.append(encoded_val)
            self.min_val = val # Aktualizujemy minimum

    def pop(self) -> None:
        if not self.stack:
            return
        
        popped = self.stack.pop()
        
        # Jeśli zdjęta wartość jest mniejsza od obecnego minimum, 
        # to znaczy, że to był nasz "zakodowany" ślad nowej epoki.
        if popped < self.min_val:
            # Odtwarzamy poprzednie minimum ze wzoru
            self.min_val = 2 * self.min_val - popped

    def top(self) -> int:
        top_val = self.stack[-1]
        # Jeśli top_val jest mniejsze od min_val, to znaczy, 
        # że leży tam zakodowany ślad, a PRAWDIWA wartość na szczycie to po prostu min_val.
        if top_val < self.min_val:
            return self.min_val
        return top_val

    def getMin(self) -> int:
        return self.min_val