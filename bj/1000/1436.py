import re
N = int(input())
count = 0
check = 1
while True:
    tmp = str(check)
    m = re.search(r'666', tmp)
    if not m == None:
        count += 1
        if count == N:
            print(check)
            break
    check += 1
