""" Assignment 1 part 1"""
operand_1 = int(input('Enter a number: '))
if operand_1 % 2 == 0:
    print('the number is divisible by 2')
else:
    print('the number is not divisible by 2')


""" Assignment 1 part 2"""
total_sum = 0
for number in range (1,51):
    total_sum += number
print("The sum of numbers from 1 to 51 is ", total_sum)
