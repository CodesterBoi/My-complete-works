def left_triangle(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*i)

left_triangle(7)

def upsidedown_right_triangle(n):
    for i in range(n,0,-1):
        print(''*(n-i)+"*"*i)

upsidedown_right_triangle(6)
