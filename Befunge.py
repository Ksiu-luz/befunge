import sys
import Instructions
import Interpreter


class Befunge:
    def __init__(self, file_name):
        try:
            with open(file_name, 'r') as f:
                self.text = f.readlines()
        except FileNotFoundError:
            sys.exit("Файл не найден")
        self.interpreter = Interpreter.Interpreter(self.text)

    def start(self, step):
        count_steps = 0
        steps = 0
        while True:
            if step and steps <= count_steps:
                print()
                steps += int(input('Введите количество шагов: '))
            e = self.interpreter.get()
            if e == ' ':
                self.interpreter.step()
                count_steps += 1
                continue
            if e.isdigit():
                self.interpreter.stack.append(int(e))
                count_steps += 1
            elif e not in Instructions.methods.keys():
                sys.exit(f'Символ не распознан: {e}')
            else:
                Instructions.methods[e](self)
                count_steps += 1
            self.interpreter.step()
            