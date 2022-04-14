###FUNTIONS###
#parameters
name = input("What is your name?\n")
last_name = input("What is your last name?\n")
bro = "brooo"

def saludo():
  print(f"Hellooo {name} {last_name}")
  

saludo()



""""
def say_hello():
  print("hellooo")

say_hello()


picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree():
  for image in picture:
    for pixel in image:
      if (pixel):
        print('*', end ="")
      else:
        print(' ', end ="")
    print(" ")

show_tree()
show_tree()
show_tree()


########################




i = 0

while i < 10:
  print("A")
  print("B")
  

  break

e = 0
while e < len([0,1,2,3,4,5,6,7,8,9,10]):
  print(e, print(len("brooo")))
  e += 1



  
def welcome():
  name = input('What is your name?\n')
  print("Hello " + name)

welcome()










some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates =[]
for value in some_list:
  if some_list.count(value) > 1:
    duplicates.append(value)

print(duplicates)










my_intro = [1]
print("Enter your personal information")
for item in my_intro:
  name = input("Name: ")

  first_surname = input("First surname: ")

  second_surname = input("Second surname: ")

  age = input("Age: ")

  nationality = input("Nationality: ")

  family = input("Has family: ")

print(f"Hello, Welcome {name}. Here is your personal information:")
print(f"You are {name} {first_surname} {second_surname}, you have {age} years old and you are {nationality}")


picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for image in picture:
  for pixel in image:
    if (pixel):
      print('*', end ="")
    else:
      print(' ', end ="")
  print('')


picture = [
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [1,2,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [1,2,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [1,2,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


for row in picture:
  for pixel in row:
    if (pixel == 1):
      print("*", end="")
    else:
      print(" ", end="")
    if (pixel == 2):
      print("O", end="")
    else:
      print(" ", end="")
  print("")

  """


print("welcome back")



#####################

puto = input("eres puto?\n")

def puto(a): 
  """
  Esta es la info de puto
  """
  print(a)

print(puto.__doc__)

#####################

#Esto es para saber si in numero tiene par

def intro(num):
  if num % 2 == 0:
    return True
  elif num % 2 != 0:
    return False
  
print(intro(50))

####################

#Esto es para limpiar el codigo de arriba

def intro(num):
  return num % 2 == 0

print(intro(50))


