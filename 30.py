print('50~100之间的偶数的和为:')
num = 50
sum = 0
while num <= 100:
    if num%2 == 0:
        sum += num
        num += 1
    num += 1
print('%d'%sum)
    
