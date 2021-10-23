# Repeat

Repeat a single character number of times.

## Usage:

Clone repository:

```bash
git clone https://github.com/endormi/repeat.git
```

Run:

```bash
usage: repeat.py [-h] -c C [-n N] [-o out]

Repeat a character number of times.

optional arguments:
  -h, --help       show this help message and exit
  -n N, --n N      repeat number of times
  -o out, --o out  PATH to output file

required arguments:
  -c C, --c C      character to repeat
```

Examples:

```bash
# displays in terminal
python repeat.py -c 0 -n 6

# Default value of -n is 6
python repeat.py -c 0

# writes to file
python repeat.py -c 0 -o file.txt
python repeat.py -c 0 -n 6 -o file.txt
```

Why?

idk
