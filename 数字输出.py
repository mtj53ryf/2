a=input("请输入一个四位数：")
b=eval(a)//1000
c=eval(a)//100%10
d=eval(a)//10%10
e=eval(a)%10
print("千位：{} 百位：{} 十位：{} 个位：{}".format(b,c,d,e))
l=[b,c,d,e]
for i in range(4):
    print(l[i],end='')