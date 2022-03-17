h=eval(input("请输入身高（米）："))
w=eval(input("请输入体重（公斤）："))
b=w/(h*h)
print("BMI值：{:.2f}".format(b))