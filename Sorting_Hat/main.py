# Write code below 💖

# Houses
G = 0
R = 0
H = 0
S = 0

print('Q1) Do you like Dawn or Dusk?')
print('  1) Dawn')
print('  2) Dusk')
question_1 = int(input('Enter answer (1-2): '))

print("\nQ2) When I'm dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')
question_2 = int(input('Enter your answer (1-4): '))

print('\nQ3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

question_3 = int(input('Enter your answer (1-4): '))

if question_1 == 1:
  G += 1
  R += 1
else:
  H += 1
  S += 1

if question_2 == 1:
  H += 2
elif question_2 == 2:
  S += 2
elif question_2 == 3:
  R += 2
elif question_2 == 4:
  G += 2
else:
  print("Wrong input.")

if question_3 == 1:
  S += 4
elif question_3 == 2:
  H += 4
elif question_3 == 3:
  R += 4
elif question_3 == 4:
  G += 4
else:
  print("Wrong input.")

print("Gryffindor:", G)
print("Ravenclaw:", R)
print("Hufflepuff:", H)
print("Slytherin:", S)

if G >= R and G >= H and G >= S:
  print("\nGryffindor!")
elif R >= H and R >= S:
  print("\nRavenclaw!")
elif H >= S:
  print("\nHufflepuff!")
else:
  print("\nSlytherin!")