""" Calculator using classes. 4 simple operations.
Keeping current answer so multiple operations are possible"""
from string import ascii_letters

class Calc:
    SIGN_TUPLE = ('+', '-', '/', '*')

    def __init__(self, a=None, o=None):
        self.answer: float = a
        self.operatiom: str = o

    def add(self, arg1: float) -> float:
        self.answer = self.answer + arg1
        return self.answer

    def decrease(self, arg1: float) -> float:
        self.answer = self.answer - arg1
        return self.answer

    def mult(self, arg1: float) -> float:
        self.answer = self.answer * arg1
        return self.answer

    def div(self, arg1: float) -> float:
        try:
            self.answer = self.answer / arg1
        except ZeroDivisionError:
            self.answer = 0.0
        return self.answer

    def set_oper(self, oper: str):
        self.operatiom = oper
        print(self.answer, self.operatiom)

    def calc(self, arg1: str):
        if self.operatiom == '+':
            print(self.add(float(arg1)))
        elif self.operatiom == '-':
            print(self.decrease(float(arg1)))
        elif self.operatiom == '*':
            print(self.mult(float(arg1)))
        elif self.operatiom == '/':
            print(self.div(float(arg1)))


def calc_main():
    calc1 = Calc()

    def inner():
        nonlocal calc1
        arg = input('input  ')
        if arg == 'reset':
            del calc1
            print('emd')
            return 'end'

        elif arg in calc1.SIGN_TUPLE:
            calc1.set_oper(arg)
        elif arg not in calc1.SIGN_TUPLE and calc1.answer is None:
            try:
                calc1.answer = float(arg)
                print(arg)
            except ValueError:
                print('input should be numeric')
        else:
            try:
                calc1.calc(arg)
            except ValueError:
                print('input should be numeric')
        inner()

    return inner()


if __name__ == '__main__':
    calc_main()
