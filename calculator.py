class Calculator:
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self):
        return self.op1 + self.op2

    def subtract(self):
        return self.op1 - self.op2

    def multiply(self):
        return self.op1 * self.op2

    def divide(self):
        return self.op1 / self.op2

# examples: 
# calc = Calculator(8, 2)
# print(calc.divide())
# funkcja divide zwróci wyjatek jesli drugim parametrem bedzie 0
# nalezy jej uzywac z try: except ZeroDivisionError:
# Teoretycznie moznaby to umiescic w konstruktorze. 
# Ale jesli metoda divide nie jest uzywana to 0 jest poprawnym argumentem