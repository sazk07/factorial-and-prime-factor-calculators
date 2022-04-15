"""
prime factors calculator
"""
int_num = input("enter number: ")
int_num = int(int_num)
listx = []
for i in range(2,int_num):
    if int_num%i == 0:
        if int_num%i not in listx:
            listx.append(i)
            i = i + 1
if listx:
    print(int_num,' is not a prime number')
else:
    print(int_num,' is a prime number')
listx2 = []
for j in listx:
    for number in range(2,j+1):
        if number not in listx2:
            if j%number ==0:
                listx2.append(number)
print('the prime factors are', listx2)
