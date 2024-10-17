x = 1
acc = 0
while x <= 624:
    print(x)
    acc += 1/((x**.5)+((x+1)**.5))
    x += 1
print(f'{acc:.3f}')