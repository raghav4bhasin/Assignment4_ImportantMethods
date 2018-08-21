new = []
x = input("Enter  numbers seperated by commas: ")
li = x.split(',')
for i in li:
    new.append(int(i))
print(new)
