with open('file1.txt','r') as f1:
    list1 = f1.read().splitlines()

with open('file2.txt','r') as f2:
    list2 = f2.read().splitlines()
print(list1)
print(list2)

result = [int(num) for num in list1 if num in list2]
print(result)