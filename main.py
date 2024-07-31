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