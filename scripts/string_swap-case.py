# https://www.hackerrank.com/challenges/swap-case/problem
# INPUT HackerRank.com presents "Pythonist 2".
# OUTPUT hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    rs = s.swapcase()
    return rs
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
