# Repeat

Repeat a character number of times.

## Usage:

Clone repository:

```
git clone https://github.com/endormi/repeat.git
```

Run:

```
usage: repeat.py [-h] -c C [-n N] [-o out]

Repeat a character number of times.

optional arguments:
  -h, --help       show this help message and exit

Required arguments:
  -c C, --c C      character to repeat

Optional arguments:
  -n N, --n N      repeat number of times
  -o out, --o out  PATH to output file
```

Examples:

```
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
