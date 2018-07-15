while True:
    word = input('查询能量请输入能量来源！退出程序请输入0:')
    print('能量来源如下：')
    print('生活缴费、行走捐、共享单车、线下支付、网络购票')
    if word == '行走捐':
        print('200')
     
    elif word == '生活缴费':
        print('300')
    
    elif word == '共享单车':
        print('350')
     
    elif word == '线下支付' :
        print('380')
    
    elif word == '网络购票':
        print('500')
    elif word == '0':
        print('已退出')
    break
    
          
