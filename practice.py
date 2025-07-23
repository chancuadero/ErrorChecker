
'''
#practice function and for loop

#define a function main
def main():
    n = int(input("What's the number? ")) #asking the user a number
    meow(n) #def a func w/c prints the nums of meow based on user's input

def meow(n):
    for i in range(n): #for loop based on the user's input
        print("meow") #prints meow based on n

main() #calling the main function

'''
'''
#practice list

students = ['Hermoine', 'Harry', 'Ron']

def studentsList():
    for student in students:
        print(student)
    
studentsList()
'''
'''
#practice dictionary

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for name, house in students.items():
    print(name, house, sep=", ")

'''
'''
#practice nested for loop with functions

def main():
    square(6)

def square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()

'''
'''
#practice dictionary

def main():
    spacecraft = {"name": "Voyager", "distance": "30 AU"}
    spacecraft.update({"orbit": "Sun"})
    print(createReport(spacecraft))

def createReport(spacecraft):
    return f"""
    Name:{spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")}
    Orbit: {spacecraft.get("orbit", "Unknown")}
    """

main()

'''

distances = {
    "Voyager 1": "163 AU",
    "Voyager 2": "136 AU"
}

def main():
    for name in distances.values():
        print(f"{name}")

main()

