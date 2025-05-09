# 첫번째 직사각형 정보
x1, y1, x2, y2 = map(int, input().split())

# 두번째 직사각형 정보
x3, y3, x4, y4 = map(int, input().split())

# mat 정의 
mat = [ [ 0 for _ in range(2001)] for _ in range(2001)] 

# 기준점
standard = 1000

# 일단 첫번째 직사각형에서는 +1
for i in range(x1, x2):
    for j in range(y1, y2):
        mat[standard + i][standard + j] += 1

# 두번쨰 직사작형에서는 +2
for i in range(x3, x4):
    for j in range(y3, y4):
        mat[standard + i][standard + j] += 2

# 범위찾기

start_x = float('inf')
start_y = float('inf')

end_x = float('-inf')
end_y = float('-inf')
for x in range(2001) :
    for y in range(2001):

        # 값을 갱신하기
        if mat[x][y] == 1 :
            if x < start_x :
                start_x = x
            
            if y < start_y :
                start_y = y

            if x > end_x :
                end_x = x 
            
            if y > end_y :
                end_y = y

ans = (end_y - start_y + 1) * (end_x - start_x + 1)
print(ans)

