
print("Arihtmetic Operators")

print("Addition: 7+9=", 7+9)

print("Substraction:7-12=", 7-12)

print("Multiplication: 7*9=", 7+9)

print("Division:16/4=", 16/4)

print("Integer division:16/4=", 16//4)

print("Modulo operator: 16%5=", 16%5)  #remainder

print("power: 2**4=", 2**4)

print("absolute:abs(-1)=", abs(-1))

prompt = "what is you name? "

name = input(prompt) # ask for ur name in the console

print("nice to meet you,", name)

"""
if name == "bob":
    print("FU bob")
else:
  print("nice to meet you,", name)
"""

prompt2 = "how old are you, " + name + "? "

age = input(prompt2)

# convert to int
age = int(age)
print("you were born in,", 2025 - age)