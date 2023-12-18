from Befunge import Befunge
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('file', type=str,
                    help='Введите название файла с инструкциями')
parser.add_argument('-s', '--step', dest='step', action='store_true',
                    help='Введите количество шагов для пошагового исполнения')
args = parser.parse_args()


if __name__ == '__main__':
    Befunge(args.file).start(args.step)
