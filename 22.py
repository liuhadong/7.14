print('-----跳一跳，输入‘退出’即可游戏-----')
print('欢迎回来，请开始游戏')   
print('请输入：中心、音乐模块、微信支付模块')
while True:   
    word = input('请输入：')

    if word == '中心':
        print('您的分数为：32')

    elif word == '音乐模块':
        print('您的分数为：30')

    elif word == '微信支付模块':
        print('您的分数为：42')

    elif word == '微信支付':
        print('输入有误，请重新输入')

    elif word == '退出':
        print('已退出')
        break


    
