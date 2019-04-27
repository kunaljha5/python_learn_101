"""Read and Print Integer Series."""
import sys

def read_series(filename):
    """
    Read the file and return the series
    :param filename: recaman's series file
    :return: series
    """
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        return [ int(line.strip()) for line in f ]
        #series = []
        #for line in f:
        #    a = int(line.strip())
        #    series.append(a)
    finally:
        f.close()
    #return series

def main(filename):
    series =  read_series(filename)
    print(series)

if __name__ == '__main__':
    main(sys.argv[1])


