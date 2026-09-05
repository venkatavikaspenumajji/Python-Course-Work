class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __floordiv__(self, other):
        return self.value // other.value

    def __mod__(self, other):
        return self.value % other.value


num1 = Number(20)
num2 = Number(6)

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)