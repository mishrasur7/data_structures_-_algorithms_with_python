from math import log10, pow

def compute_arithmetic():
    a = int(input())
    b = int(input())
    print(f'{a} + {b} is {a + b}')
    print(f'{a} - {b} is {a - b}')
    print(f'{a} * {b} is {a * b}')
    print(f'{a} / {b} is {a / b}')
    print(f'{a} % {b} is {a % b}')
  #  print(f'The result of log10 {a} is {log10(a)}')
    print(f'{a} ^ {b} is {int(pow(a, b))}')

compute_arithmetic()