# Madlib = word game where user is  substituing the blank area without knowing the story
# Concatenation (putting strings together
# Like "Hey ___"

# person = input("") 
# print("Hey " + person) # Simple way
# print("Hey {}".format(person)) # Format method
# print(f"Hey {person}") # F-string

adj = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
famous_person = input("Enter a famous person's name: ")

madlib = f"Computer programming is so {adj} that I love it!" \
    f" I wish I could {verb1} it all day. Stay hydrated and {verb2} like a {famous_person}!"
    
print(madlib)