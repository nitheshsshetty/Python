from art import logo
from replit import clear

def add(a,b):
  ''' Return a value after it adds 2 numbers'''
  return a+b
def sub(a,b):
  ''' Return a value after it substracts 2 numbers'''
  return a-b
def mul(a,b):
  ''' Return a value after it multiply 2 numbers'''
  return a*b
def div(a,b):
  ''' Return a value after it divide 2 numbers'''
  return a/b

operation ={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}
def display_operations():
 print(" +")
 print(" -")
 print(" *")
 print(" \\")
 return

cont = 'y'
op=''
first = 'yes'
while cont == 'y' :
  if first == 'yes':
    print(logo)
    value=int(input("What's the first number? : "))
    display_operations()
    op=input("Pick an operation : ")
  
  if first != 'yes':
    op=input("Pick an operation : ")
  
  num=int(input("What's the next number? : "))
  func=operation[op]
  copy=value
  value=func(value,num)
  print(f"\n {copy} {op} {num} = {value}")
  cont=input(f"\n Type 'y' to continue calculating with {value} or type 'n' to start a new calculation: ")
  if cont == 'n':
    clear()
    cont = 'y';
    first = 'yes'
  else:
    first = 'no'
