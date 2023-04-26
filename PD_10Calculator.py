# The program contains a module name replit from replit website.
from art import logo
from replit import clear
def start():
  print (logo)
  n1 = int(input("What's the first number:"))
  operation = ["+","-","*","/"]
  for i in operation:
    print(i)
  o = input("Pick an operation:")
  calculator(n1,o)
  
def calculator(n1,o):
  while True:
    n2 = int(input("What's the next number:"))
    if o == "+":
      ans = n1+n2
    elif o == "-":
      ans = n1-n2
    elif o == "*":
      ans = n1*n2
    else:
      ans = n1/n2
    print(f"{n1}{o}{n2} = {ans}")
    a = input(f"Type 'y' to continue calculation with {ans}, and 'n' to start a new calculation.")
    if a == "y":
      n1 = ans
      o = input("Pick an operation:") 
    elif a == "n":
      clear()
      start()
      
start()
