num = 100
while num<=999:
    a = num//100
    b = (num//10)%10
    c = num%10
    if num == a**3+b**3+c**3:
        print('%d'%num)
    num+=1
