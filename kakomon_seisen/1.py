a, b = map(int, input().split())
# 0 is False, other numbers are True. 
if (a * b) % 2:
    print("Odd")
else:
    print("Even")
