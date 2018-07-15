age = int(input('年龄:'))
subject = input('专业:')
college = input('是否重点大学:')
if (subject == '电子信息工程专业' and age > 25)or(subject == '电子信息工程专业' and college == '是')or(age < 28 and subject == '计算机专业'):
    print('恭喜面试通过')
else:
    print('抱歉，您未达到面试要求')
