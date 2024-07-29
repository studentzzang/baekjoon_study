import math

x = int(input())

for i in range(x):
        
    x1,y1, r1, x2, y2, r2= map(float, input().split())

    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if (dis == 0 and r1==r2): # 무한 만남 (중심같음, 반지름같음)
        print(-1)
    
    elif (dis == abs(r2-r1) or dis == abs(r2+r1)): # 내접 or 외접
        print(1)

    elif (dis > abs(r2-r1) and dis < abs(r2+r1)):
        print(2)
    
    else:
        print(0)
    


