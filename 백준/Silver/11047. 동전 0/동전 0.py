N, K = map(int, input().split())

Coins = []
Count = 0 

for i in range(N):
	Coin = int(input())
	Coins.append(Coin) # 1 5 10 ... 5000 10000

Coins.reverse() # 10000 5000 ... 10 5 1 

for Coin in Coins:
	Count += K // Coin
	K -= (K // Coin) * Coin

print(Count)
