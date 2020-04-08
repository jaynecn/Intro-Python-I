# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
  if num % 2 ==0:
    return True
  
print(is_even(2))
  

# Read a number from the keyboard
num = input("Enter a number: ")
jayne = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def printer(jayne):
  if jayne % 2 == 0:
    print("Even!")
  else: print("Odd!")

printer(jayne)