while True:
    num = int(input('请输入数字：'))
    if num == 0:
        print('')
        
    elif num < 100 and num > 0: 
        print('命运给予我们的不是失望之酒，而是机会之杯'*num)
 
    elif num == 100:
        print('结束')
        break
