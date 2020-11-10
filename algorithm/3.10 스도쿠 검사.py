sdoku=[]

for i in range(9):
    sdoku.append(list(map(int,input().split())))
for i in range(9):
    for num in range(1,10):
        if num in sdoku[i]:
            continue
        else:
            print('NO')
            exit()
for j in range(9):
    temp=[]
    for i in range(9):
        temp.append(sdoku[i][j])
    for num in range(1,10):
        if num in temp:
            continue
        else:
            print('NO')
            exit()

for i in range(3):
    for j in range(3):
        temp=[]
        for k in range(3*i,3*(i+1)):
            for l in range(3*j,3*(j+1)):
                temp.append(sdoku[k][l])

        for num in range(1,10):
            if num in temp:
                continue
            else:
                print('NO')
                exit()
print('YES')
