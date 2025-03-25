# Story
def generate_madlib(adj1, adj2, adj3, adj4, verb1, verb2, verb3, verb4, verb5, verb6, verb7, verb8, person1, person2):
    story = f"""
    One {adj1} morning, {person1} decided to {verb1} to the park. It was a {adj2} day, and the sky looked perfect for {verb2}.

    On the way, {person1} met {person2}, who was trying to {verb3} a {adj3} kite. They both laughed and decided to {verb4} together.

    Suddenly, a {adj4} dog ran past them, causing {person2} to {verb5} into a puddle. Without missing a beat, {person1} helped them {verb6} up.

    They spent the rest of the day {verb7} and {verb8} until the sun went down.

    What a day to remember!
    """
    return story

# User inputs
if __name__ == "__main__":
    madlib = generate_madlib(
adj1=input("Enter an adjective: "), adj2=input("Enter an adjective: "), adj3=input("Enter an adjective: "), adj4=input("Enter an adjective: "),
verb1=input("Enter a verb: "), verb2=input("Enter a verb: "), verb3=input("Enter a verb: "), verb4=input("Enter a verb: "),
verb5=input("Enter a verb: "), verb6=input("Enter a verb: "), verb7=input("Enter a verb ending in -ing: "), verb8=input("Enter a verb ending in -ing: "),
person1=input("Enter a person's name: "), person2=input("Enter a person's name: ")
    )
    print(madlib)