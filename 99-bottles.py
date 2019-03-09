''' 
    Sings the children's song '99 
    Bottles of beer on the wall'. 
    Takes in an integer as an input, 
    and counts down until zero.
'''

def sing(bottles):
  if bottles <= 0: return None
  n = bottles
  while (n >= 0):
    if (n == 1) == True:
      objects = "bottle"
      objectsMinusOne = "bottles"
    elif (n == 2) == True:
      objects = "bottles"
      objectsMinusOne = "bottle"
    else:
      objects = "bottles"
      objectsMinusOne = "bottles"
    if (n > 0):
      print(str(n) + " " + objects + " of beer on the wall, " + str(n) + " " + objects + " of beer.")
      print("Take one down and pass it around, " + str(n - 1) + " " + objectsMinusOne + " of beer on the wall.")
      print(" ")
    elif (n == 0):
      print("No more bottles of beer on the wall, no more bottles of beer.")
      print("Go to the store and buy some more, " +  str(bottles) +" bottles of beer on the wall.")
    else:
      print("Error: Where's the booze?")
    n -= 1

print("Enter number of bottles of beer on the wall:")
sing(int(input()))

