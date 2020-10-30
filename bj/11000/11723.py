from sys import stdin, stdout
read = lambda : stdin.readline()

def solve():
    N = int(read())
    S = set()
    for _ in range(N):
        inst =  read()
        save = inst.split()
        if save[0] == 'add':
            S.add(save[1])
        elif save[0] == 'remove':
            S.discard(save[1])
        elif save[0] == 'check':
            if save[1] in S:
                stdout.write('1\n')
            else:
                stdout.write('0\n')
        elif save[0] == 'toggle':
            if save[1] in S:
                S.remove(save[1])
            else:
                S.add(save[1])
        elif save[0] == 'all':
            for i in range(1, 21):
                S.add(str(i))
        elif save[0] == 'empty':
            S = set()




if __name__ == '__main__':
    solve()
