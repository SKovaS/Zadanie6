mas=[25,10,5,1]
n=-1
count=0
while n<0:
    print("O hai! How much change is owed?\n")
    n=float(input())
    n=n*100
    n=round(n)
for i in range(0,4):
    while n>=mas[i]:
        n=n-mas[i]
        count=count+1
print(count)