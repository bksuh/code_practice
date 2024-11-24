import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    overlap_left = max(x1, x3)
    overlap_right = min(x2, x4)
    overlap_bottom = max(y1, y3)
    overlap_top = min(y2, y4)
    

    if overlap_left < overlap_right and overlap_bottom < overlap_top:
        overlap_area = (overlap_right - overlap_left) * (overlap_top - overlap_bottom)
    else:
        overlap_area = 0
    rect1_area = (x2 - x1) * (y2 - y1)
    non_overlap_area = rect1_area - overlap_area
    
    print(non_overlap_area)
