import sys
import Instructions
import Interpreter


class Befunge:
    def __init__(self, file_name):
        try:
            with open(file_name, 'r') as f:
                self.text = f.read().split("\n")
        except FileNotFoundError:
            sys.exit("Файл не найден")
        self.interpreter = Interpreter.Interpreter(self.text)

    def start(self):
        while True:
            e = self.interpreter.get()
            if e == ' ':
                self.interpreter.step()
                continue
            if e.isdigit():
                self.interpreter.stack.append(int(e))
            elif e not in Instructions.methods.keys():
                sys.exit(f'Символ не распознан: {e}')
            else:
                Instructions.methods[e](self)
            self.interpreter.step()
            