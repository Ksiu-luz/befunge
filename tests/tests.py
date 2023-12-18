import unittest
import Instructions
from Befunge import Befunge
from Interpreter import Interpreter


class InterpreterTest(unittest.TestCase):
    def test_pointer(self):
        self.assertEqual(Interpreter('<').get(), '<')

    def test_step(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.step()
        self.assertEqual(befunge.interpreter.x, 0)
        self.assertEqual(befunge.interpreter.y, 1)

    def test_add(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(5)
        befunge.interpreter.stack.append(7)
        Instructions.add(befunge)
        self.assertEqual(befunge.interpreter.stack.pop(), 12)

    def test_sub(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(5)
        befunge.interpreter.stack.append(7)
        Instructions.sub(befunge)
        self.assertEqual(befunge.interpreter.stack.pop(), -2)

    def test_mul(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(5)
        befunge.interpreter.stack.append(7)
        Instructions.mul(befunge)
        self.assertEqual(befunge.interpreter.stack.pop(), 35)

    def test_floordiv(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(5)
        befunge.interpreter.stack.append(7)
        Instructions.floordiv(befunge)
        self.assertEqual(befunge.interpreter.stack.pop(), 0)

    def test_mod(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(5)
        befunge.interpreter.stack.append(7)
        Instructions.mod(befunge)
        self.assertEqual(befunge.interpreter.stack.pop(), 5)

    def test_random(self):
        befunge = Befunge('../programs/hello.txt')
        Instructions.random_vector(befunge)
        self.assertIn(befunge.interpreter.vector, ['^', 'v', '>', '<'])

    def test_greater(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(5)
        befunge.interpreter.stack.append(7)
        Instructions.greater(befunge)
        self.assertEqual(befunge.interpreter.stack.pop(), 0)

    def test_negative(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(1)
        Instructions.negative(befunge)
        self.assertEqual(befunge.interpreter.stack.pop(), 0)

    def test_double(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(1)
        Instructions.double(befunge)
        self.assertEqual(befunge.interpreter.stack.pop(), 1)
        self.assertEqual(befunge.interpreter.stack.pop(), 1)

    def test_step_up_or_down(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(0)
        Instructions.step_up_or_down(befunge)
        self.assertEqual(befunge.interpreter.vector, 'v')

    def test_step_left_or_right(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(0)
        Instructions.step_left_or_right(befunge)
        self.assertEqual(befunge.interpreter.vector, '>')

    def test_swap(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(0)
        befunge.interpreter.stack.append(50)
        Instructions.swap(befunge)
        self.assertEqual(befunge.interpreter.stack.pop(), 0)
        self.assertEqual(befunge.interpreter.stack.pop(), 50)

    def test_delete(self):
        befunge = Befunge('../programs/hello.txt')
        befunge.interpreter.stack.append(1)
        befunge.interpreter.stack.append(2)
        befunge.interpreter.stack.append(555)
        Instructions.delete(befunge)
        self.assertEqual(befunge.interpreter.stack.pop(), 2)

    def test_right(self):
        befunge = Befunge('../programs/hello.txt')
        Instructions.right(befunge)
        self.assertEqual(befunge.interpreter.vector, '>')

    def test_left(self):
        befunge = Befunge('../programs/hello.txt')
        Instructions.left(befunge)
        self.assertEqual(befunge.interpreter.vector, '<')

    def test_up(self):
        befunge = Befunge('../programs/hello.txt')
        Instructions.up(befunge)
        self.assertEqual(befunge.interpreter.vector, '^')

    def test_down(self):
        befunge = Befunge('../programs/hello.txt')
        Instructions.down(befunge)
        self.assertEqual(befunge.interpreter.vector, 'v')

    def test_text(self):
        interpreter = Befunge('../programs/hello.txt')
        self.assertEqual(interpreter.text[1][0], '@')


if __name__ == '__main__':
    unittest.main()
