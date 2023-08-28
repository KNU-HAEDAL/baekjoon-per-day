N, r, c = map(int, input().split())

def gogo(N, r, c):

	if N == 0:
		return 0
        
	return 2*(r%2)+(c%2) + 4*gogo(N-1, int(r/2), int(c/2))

print(gogo(N, r, c))
