n=[int(i) for i in input().split()]

if n[0]%4==0:
    if n[1]==1:
        print("JO")
    else:
        print("GANGPLANK")
else:
    if n[1]==0:
        print("JO")
    else:
        print("GANGPLANK")
