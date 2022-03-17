a=input("请输入一个四位数：")
b=eval(a)//1000
c=eval(a)//100%10
d=eval(a)//10%10
e=eval(a)%10
l=[b,c,d,e]
for i in range(4):
    l[i]+=5
    l[i]%=10
for i in range(2):
    l[i],l[3-i]=l[3-i],l[i]
for i in range(4):
    print(l[i], end='')