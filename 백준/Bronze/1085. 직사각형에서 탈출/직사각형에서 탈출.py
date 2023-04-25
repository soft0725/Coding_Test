x, y, w, h = map(int, input().split())

min_dis = [abs(0 - x), abs(0 - y), abs(w - x), abs(h - y)]
min_dis.sort()

print(min_dis[0])