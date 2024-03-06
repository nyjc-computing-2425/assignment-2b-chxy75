num = input('Enter a number (decimal only): ')
# type your code here
point = num.find('.')
decimal = num[point:]
dp = len(decimal.lstrip(' ')) - 1
# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
