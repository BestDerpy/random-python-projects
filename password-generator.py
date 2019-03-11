'''
    Basic password generator.
    Takes in a string consisting only of one or 
    two-digit integers as input,
    and returns a randomly generated password.
'''

def passwordMaker():
  import random
  import re
  alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  minPassLength = 0
  password = ''
  length = input('Enter password length: ')

  while not(re.match(r"^([1-9]\d|[1-9])$", length)):
    print("Why'd you type a string?")
    length = input("Enter a number (two digits maximum): ")

  length = int(length)

  while minPassLength < length:
    password += random.choice(alpha)
    minPassLength = len(password)
  print("Password generated!")
  print(password)


passwordMaker()