# https://www.acmicpc.net/problem/2839
# 설탕 배달
# 29200 KB / 72 ms


bag_adj = [(0, 0), (-1, 2), (-2, 4), (0, 1), (-1, 3)]
bag_add = [sum(b) for b in bag_adj]
q, r = divmod(int(input()), 5)
num_bags = q + bag_add[r] if q >= -bag_adj[r][0] else -1

print(num_bags)