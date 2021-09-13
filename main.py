import random
import calculator
rand_list = []
for i in range(20):
   n = random.randint(1,100)
   rand_list.append(n)
print(rand_list)
print('=======')





First=random.choice(rand_list)
Second=random.choice(rand_list)
print(f"First number{First}")
print(f"Second number{Second}")

# x = int(input("введите дополнительное число"))

p1=calculator.calculator().plus(First,Second,)
p2=calculator.calculator().minus(First,Second)
p3=calculator.calculator().multiply(First,Second)
p4=calculator.calculator().divide(First,Second)
print('========')
# print(p1)
# print(p2)
# print(p3)
# print(p4)

