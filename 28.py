a, b = 0, 1

for i in range(100):
    print(a)
    # c = a
    # a = b
    # b = c+b
    a, b = b, a + b

# 0,1,1,2,3,5,8,13,21,...
