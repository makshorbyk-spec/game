print("hello world")
import random
name1 = random.randint(1, 10)
name2 = int(input("число 1 10 ")) 
result1 = name1 < name2
print (result1)
print("ворог загадав число")
print (name1)
if result1 == True:
  print("твоє число біше")
else:
  print("Твоє число менше або дорівнює")