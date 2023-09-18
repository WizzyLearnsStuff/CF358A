from itertools import combinations as c

def main():
    a = int(input())

    if a <= 3:
        print("no")
        return
        
    b = map(int, input().split())
    l = []
    x0 = next(b)
    for i in b:
        l.append((min(x0, i), max(x0, i)))
        x0 = i

    for i, j in c(l, 2):
        if i[0] < j[0] < i[1] < j[1] or j[0] < i[0] < j[1] < i[1]:
            print("yes")
            return

    print("no")

main()
