class Utils:
    def __init__(self):
        pass

    @staticmethod
    def reversed(number: int):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")

        # check for negative numbers
        is_negative = False
        if number < 0:
            is_negative = True
            number = abs(number)

        return int(str(number)[::-1]) if not is_negative else -int(str(number)[::-1])

    @staticmethod
    def formatter(number: int):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")

        binary = bin(number)
        octal = oct(number)

        return binary, octal


if __name__ == '__main__':
    print(Utils.reversed(-12345))
    print(Utils.formatter(-12345))
