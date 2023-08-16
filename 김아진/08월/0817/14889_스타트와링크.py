import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
team_distance = []
team_list = list(combinations(range(n), n//2))

def get_team_stat(team):
    stat = 0
    for i in range(n//2 - 1):
        for j in range(i+1, n//2):
            a, b = team[i], team[j]
            stat += stats[a][b] + stats[b][a]
    return stat


team_len = len(team_list)
for i in range(team_len // 2):
    a = get_team_stat(team_list[i])
    b = get_team_stat(team_list[(team_len - 1) - i])
    team_distance.append(abs(a-b))

print(min(team_distance))