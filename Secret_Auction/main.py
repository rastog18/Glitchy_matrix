#Replit was a module created by the teacher.
from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print (logo)
auction = {}
v_max = 0
k_max = ""
while True:
  key = input("What's your name ?:")
  value = int(input("Enter your bid:"))
  auction [key] = value
  a = input("Are there any other bidders ? Type 'yes or 'no':")
  if a == "yes":
    clear()
  else:
    break
for key in auction:
  value = auction[key]
  if v_max < value:
    v_max = value
    k_max = key
print(f"The winner is {k_max},with a bid of ${v_max}")
