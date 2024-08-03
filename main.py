# 2.0
print("Hello world!")

# 2.3
booleanVal = True # False | true, false가 아니라니

# 2.4 2.6 2.7
def sayHello(name):
  print('Hello!', name)

sayHello("Minung")
# sayHello("Minung", 123) # error

# 2.9
def sayHelloWithDefault(name = "min"):
  print('Hello!', name)

sayHelloWithDefault()

# 2.10
def plus(a, b):
  return a + b;

print(plus(1, 2))

# 2.11
name = "Minung"
print(f"Hello {name}") # f는 format의 의미

# 3.0
condition = True
if condition:
  print("true!")
else:
  print("False!")


# 3.1 elif
winner = 10
if winner > 10:
  print("winner > 10")
elif winner < 10:
  print("winner < 10")
else:
  print("10!")

# 3.3 and or

print(True and False) # 키워드로 접근이라니 특이하네
print(True or False)