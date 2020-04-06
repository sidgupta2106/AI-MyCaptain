n = int(input("Enter the number of elements in a list\n"))
lst = list(map(int, input("Enter a list of numbers").strip().split()))[:n]
x = []
print("\nInput List:", lst)
for i in lst:
    if(i>0):
        x.append(i)

print("\nOutput List:", x)
