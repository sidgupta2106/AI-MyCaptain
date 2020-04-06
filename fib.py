n = int(input("Enter the number of Fibonacci terms\n"))
f0, f1 = 0, 1
f2 = 1
i = 0
print("0 \n 1")
while (i<=n):
    f0 = f0+f1
    f1 = f1+f2
    print(f0,"\n", f1)
    f2 = f0+f1
    i+=1