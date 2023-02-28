with open('27-B_2.txt') as f:
    maxx_none = 0
    maxx_14 = 0
    maxx_7 = 0
    maxx_2 = 0
    none = f.readline()
    sp = [int(i) for i in f]
    for i in sp:
        if i % 14 == 0:
            maxx_14 = max(maxx_14,i)
        elif i % 7 == 0:
            maxx_7 = max(maxx_7,i)
        elif i % 2 == 0:
            maxx_2 = max(maxx_2,i)
        else:
            maxx_none = max(maxx_none,i)
    print(max(maxx_14*max(maxx_2,maxx_7,maxx_none),maxx_2*maxx_7))