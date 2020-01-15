import random
right=0
wrong=0
aaa=0
while True:
    y=input("你想玩多少以内的加减法:")
    try:
        if float(y)>=1:
            break
        else:
            print("输入有误，重新输入")
    except:
        y.strip()==""
        print("输入有误，重新输入")
while True:
    try:
        print("运算选择")
        print("1.加法 2.减法")
        z=input()
        if float(z)==1:
            input("回车以开始，游戏中回车以结束")
            while True:
                a=random.randint(1,float(y)-1)
                b=random.randint(1,float(y)-a)
                print(a,"+",b,"=",sep="")
                x=input()
                try:
                    if float(x)!=a+b:
                        print("错误")
                        wrong=wrong+1
                        aaa=aaa+1
                    else:
                        print("正确")
                        right=right+1
                        aaa=aaa+1
                except:
                    x.strip()==""
                    break

            break
        elif float(z)==2:
            input("回车以开始，游戏中回车以结束")
            while True:
                a=random.randint(1,float(y)-1)
                b=random.randint(1,a-1)
                print(a,"-",b,"=",sep="")
                x=input()
                try:
                    if float(x)!=a-b:
                        print("错误")
                        wrong=wrong+1
                        aaa=aaa+1
                    else:
                        print("正确")
                        right=right+1
                        aaa=aaa+1
                except:
                    x.strip()==""
                    break
            break
        else:
            input("输入有误，请重输")
    except:
        z.strip()==""
print("正确",right,"次",sep="")
print("错误",wrong,"次",sep="")
print("一共做了",aaa,"题",sep="")
if right==aaa and aaa>=1:
    print("全对了，真厉害！")
    input("回车以退出")
elif 0.5*aaa<=right and aaa>=1:
    print("还不错，对了不少呢！")
    input("回车以退出")
else:
    print("不行哦，再接再厉吧！")
    input("回车以退出")
