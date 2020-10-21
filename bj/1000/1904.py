N = int(input())
f = 1
s = 2
tmp = 0
for i in range(N-1):
    tmp = f
    f = s
    s = (tmp+s) % 15746
print(f)
