class calculator():

    def add(self, a,b):
        sum=a+b
        print(sum)

    def sub(self,a,b):
        minus=a-b
        print(minus)

    def div(self, a,b):
        divi=a/b
        print(divi)

op = calculator()
op.div(2,3)


n=[]
for i in range(1,11):
    if i % 2 !=0:
        n.append(i)

print(n)

x = 15
y = 17

if x < 25:
    if y < x:
        print("y is less than x")
    elif y == x:
        print("y is same as x")
    else:
        print("y is less than x and y is not same as x")


for i in range(1,6):
    if i==3:
        continue
    print(i)#1, 2,






