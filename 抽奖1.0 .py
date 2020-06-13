import random
import time
a=0
b=0
c=0
list1=[]
list2=[]
while True:
    new=input('请输入姓名：')
    if new.strip()=="" :
        break
    else:
        list1.append(new)
print('请确认抽奖名单')
print(list1)
people=int(input('请输入中奖人数：'))
total=len(list1)
input('回车以开始抽奖')
while b<people:
    c=random.randint(0,total-1)
    list2.append(list1[c])
    if len(list2) != len(set(list2)):
        list2 = sorted(set(list2), key=list2.index)
        b=b-1
    b=b+1
print('正在抽奖',end='')
time.sleep(0.5)
while a<6:
    print('.',end='')
    time.sleep(0.5)
    a=a+1
print()
print('中奖名单如下：')
print(list2)
input()
