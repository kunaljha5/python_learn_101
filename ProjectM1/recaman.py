import sys
from itertools import count, islice

def sequence():
    """
    Genrate Recaman's Sequence.
    :return:
    """
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c
def write_sequence(filename, num):
    """
    Write Recaman's Sequence to a text file.
    :param filename: text file
    :param num: upper limit
    :return:
    """
    f = open(filename, mode='wt', encoding='utf-8')

    for r in islice(sequence(), num + 1):
        f.writelines("{0}\n".format(r))
    f.close()
if __name__ == '__main__':
    write_sequence(filename=sys.argv[1], num=int(sys.argv[2]))





