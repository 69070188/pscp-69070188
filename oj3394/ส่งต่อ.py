"""ส่งต่อ"""
def main():
    """ส่งต่อ"""
    d = input().split()
    n = int(d[0])
    s = int(d[1])

    nxt = [0] * (n + 1)
    i = 1
    while i <= n:
        nxt[i] = int(input())
        i += 1

    vis = [False] * (n + 1)
    cur = s
    while cur and not vis[cur]:
        vis[cur] = True
        cur = nxt[cur]

    cnt = 0
    i = 1
    while i <= n:
        if vis[i]:
            cnt += 1
        i += 1

    print(cnt)
main()
