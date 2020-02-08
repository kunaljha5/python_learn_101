# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product



if __name__ == '__main__':
    K,M = map(int,input().split())
    N = (list(map(int, input().split()))[1:] for _ in range(K))
    # print(list(N))
    results = map(lambda x: sum(pow(i,2) for i in x)%M, product(*N))
    print(max(results))
