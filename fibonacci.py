def fibonacci():
    "Fibonacci sequence generator"
    (a, b) = (1, 1)
    yield from (a, b)
    while True:
        (a, b) = (b, a + b)
        yield b


class NumberLengthChecker:
    def __init__(self, length):
        self._min_number = 10 ** (length - 1)

    def is_long_enough(self, number):
        "Checks if the number is at least <length> digits"
        return self._min_number <= number