import sys
sys.stdin = open("./Algorithm/Day4세금 징수.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    Tax = int(input())

    listCoin = [50000, 10000, 5000, 1000, 500, 100]

    countCoin = 0
    for coin in listCoin:
        countCoin += Tax // coin
        Tax %= coin

    print(countCoin)
