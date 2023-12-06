from Befunge import Befunge
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('file', type=str)
args = parser.parse_args()


if __name__ == '__main__':
    Befunge(args.file).start()
