import random

def wer(a,b):
    c=random.randint(a,b)
    return c
  

a=int(input("Введите число"))
b=int(input("Введите число"))

res = wer(a,b)
print("Ваше число:",res)
