import sys

_dp = [[0 for row in range(2)]for col in range(41)]
_dp[0] = [1,0]
_dp[1] = [0,1]

def fibo(n) :
    if n == 0 or n ==1 :
        return _dp[n]
    for i in range(2,n+1):
        _dp[i][0] = _dp[i-1][0] + _dp[i-2][0]
        _dp[i][1] = _dp[i-1][1] + _dp[i-2][1]
    return

def main():
    fibo(40)
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        print(_dp[n][0], _dp[n][1])

main()
