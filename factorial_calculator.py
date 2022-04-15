""" factorial calculator """
enter_factorial = input('enter number for which you want factorial: ')
factorial_number = int(enter_factorial)
FIRST_FACTORIAL = 1
for i in range (1,factorial_number):
    FIRST_FACTORIAL = FIRST_FACTORIAL * (i+1)
print(f"{factorial_number}! is {FIRST_FACTORIAL}")
