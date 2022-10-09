#3. Write a script which accepts a <number> from user and print
#out a sum of the first <number> positive integers.

m = 'введіть число:'
print(f'{m:.^30}')
x = int(input())
sum_number = sum(range(x+1))
print('сума числа:', x,'є:', sum_number)
