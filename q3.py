from random import randint
for i in range(10):
  a = randint(0,9)
  b = randint(0,9)
  guess = int(input("Question 1: "+str(a)+" x "+str(b)+" = "))
  if(guess == a*b):
    print("Right!")
  else:
    print("Wrong. The answer is",a*b,".")
