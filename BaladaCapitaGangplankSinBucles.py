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

'''
[1,2,3] #Primero
[4] -> [1,2,3] #Segundo
[5,6,7] -> [4] -> [1,2,3] #Primero
[8] -> [5,6,7] -> [4] -> [1,2,3] #Segundo
[9,10,11]->[8] -> [5,6,7] -> [4] -> [1,2,3] #Primero
[12] ->[9,10,11]->[8] -> [5,6,7] -> [4] -> [1,2,3] #Primero
'''
