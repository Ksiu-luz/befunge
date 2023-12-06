import sys
from random import choice


def right(symbol):
    symbol.interpreter.vector = '>'


def left(symbol):
    symbol.interpreter.vector = '<'


def up(symbol):
    symbol.interpreter.vector = '^'


def down(symbol):
    symbol.interpreter.vector = 'v'


def step_left_or_right(symbol):
    if symbol.interpreter.stack.pop():
        symbol.interpreter.vector = '<'
    else:
        symbol.interpreter.vector = '>'


def step_up_or_down(symbol):
    if symbol.interpreter.stack.pop():
        symbol.interpreter.vector = '^'
    else:
        symbol.interpreter.vector = 'v'


def random_vector(symbol):
    symbol.interpreter.vector = choice(['^', 'v', '>', '<'])


def next_point(interpreter):
    interpreter.interpreter.step()


def end(interpreter):
    sys.exit()


def double(interpreter):
    a = interpreter.interpreter.stack.pop()
    interpreter.interpreter.stack.append(a)
    interpreter.interpreter.stack.append(a)


def swap(symbol):
    a = symbol.interpreter.stack.pop()
    try:
        b = symbol.interpreter.stack.pop()
    except IndexError:
        b = 0
    symbol.interpreter.stack.append(a)
    symbol.interpreter.stack.append(b)


def delete(symbol):
    symbol.interpreter.stack.pop()


def put(symbol):
    x = symbol.interpreter.stack.pop()
    y = symbol.interpreter.stack.pop()
    value = symbol.interpreter.stack.pop()
    symbol.interpreter.board[x][y] = chr(value)


def get(symbol):
    x = symbol.interpreter.stack.pop()
    y = symbol.interpreter.stack.pop()
    value = symbol.interpreter.board[x][y]
    symbol.interpreter.stack.append(ord(value))


def string(interpreter):
    interpreter.interpreter.step()
    e = interpreter.interpreter.get()
    while e != '\"':
        interpreter.interpreter.stack.append(e.encode('ASCII'))
        interpreter.interpreter.step()
        e = interpreter.interpreter.get()


def add(symbol):
    b = symbol.interpreter.stack.pop()
    a = symbol.interpreter.stack.pop()
    symbol.interpreter.stack.append(a + b)


def sub(symbol):
    b = symbol.interpreter.stack.pop()
    a = symbol.interpreter.stack.pop()
    symbol.interpreter.stack.append(a - b)


def mul(symbol):
    b = symbol.interpreter.stack.pop()
    a = symbol.interpreter.stack.pop()
    symbol.interpreter.stack.append(a * b)


def floordiv(symbol):
    b = symbol.interpreter.stack.pop()
    a = symbol.interpreter.stack.pop()
    if b == 0:
        symbol.interpreter.stack.append(0)
    else:
        symbol.interpreter.stack.append(a // b)


def mod(symbol):
    b = symbol.interpreter.stack.pop()
    a = symbol.interpreter.stack.pop()
    symbol.interpreter.stack.append(a % b)


def negative(interpreter):
    if interpreter.interpreter.stack.pop() == 0:
        interpreter.interpreter.stack.append(1)
    else:
        interpreter.interpreter.stack.append(0)


def greater(symbol):
    a = symbol.interpreter.stack.pop()
    b = symbol.interpreter.stack.pop()
    if b > a:
        symbol.interpreter.stack.append(1)
    else:
        symbol.interpreter.stack.append(0)


def input_number(interpreter):
    a = input('Введите число: ')
    if a.isdigit():
        interpreter.interpreter.stack.append(int(a))
    else:
        sys.exit('Это не число')


def input_symbol(symbol):
    a = input('Введите символ(не число): ')
    if a.isdigit():
        sys.exit('Это число')
    symbol.interpreter.stack.append(a[0].encode('ASCII'))


def print_number(symbol):
    a = symbol.interpreter.stack.pop()
    print(str(a), end='')


def print_symbol(symbol):
    a = symbol.interpreter.stack.pop().decode('ASCII')
    print(a, end='')


methods = {'>': right,
           '<': left,
           '^': up,
           'v': down,
           '_': step_left_or_right,
           '|': step_up_or_down,
           '?': random_vector,
           '#': next_point,
           '@': end,
           ':': double,
           '\\': swap,
           '$': delete,
           'p': put,
           'g': get,
           '\"': string,
           '+': add,
           '-': sub,
           '*': mul,
           '/': floordiv,
           '%': mod,
           '!': negative,
           '`': greater,
           '&': input_number,
           '~': input_symbol,
           '.': print_number,
           ',': print_symbol}
