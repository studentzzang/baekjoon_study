import math

x = int(input())


for i in range(x):
        
    x1,y1, r1, x2, y2, r2= map(float, input().split())

    if x1==x2 and y1==y2 and r1==r2: # 위치, 반지름 같음
        print(-1)
    elif x1==x2 and y1==y2 and r1!=r2:  # 위치 같고 반지름 다름 (겹침 없음)
        print(0)

    elif math.sqrt(x2-x1)
    
