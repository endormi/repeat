import argparse
import sys
from charred import repeat_char


def main():
    parser = argparse.ArgumentParser(description='Repeat a single character number of times.')
    parser.add_argument("-c", metavar='C', type=str, required=True,
                        help='character to repeat')
    parser.add_argument("-n", metavar='N', type=int, default=6,
                        help='repeat number of times')
    parser.add_argument("-o", metavar='out', type=str, default=False,
                        help='PATH to output file')
    args = parser.parse_args()

    if len(args.c) != 1:
        print("Too many characters, only use 1.")
        sys.exit()

    output = repeat_char(args.c, args.n)

    if args.o:
        with open(args.o, "w") as f:
            f.write(output)
    else:
        print(output)


if __name__ == '__main__':
    main()
