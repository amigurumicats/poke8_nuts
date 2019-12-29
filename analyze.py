import sys

# n回振る
def strategy_0(n, data):
    return sum(sum(d[:n]) for d in data)

# n個以上とれるまで振る
def strategy_1(n, data):
    res = 0
    for d in data:
        now = 0
        for i in d:
            now += i
            if now >= n: break
        res += now
    return res


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        data = [list(map(int, line.strip().split(','))) for line in f]

    for i in range(1, 15):
        res = strategy_0(i, data)
        print(f'{i}回振る : {res} ({res/len(data):.3f})')

    for i in range(1, 20):
        res = strategy_1(i, data)
        print(f'{i}個以上とれるまで振る : {res} ({res/len(data):.3f})')
