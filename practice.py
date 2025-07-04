#meow

#define a function main
def main():
    n = int(input("What's the number? ")) #asking the user a number
    meow(n) #def a func w/c prints the nums of meow based on user's input

def meow(n):
    for i in range(n): #for loop based on the user's input
        print("meow") #prints meow based on n

main() #calling the main function
