C = 300000000

def main():
    userInput = input("Enter mass...")
    convertMassToJule(userInput)

def convertMassToJule(mass):
    print(str(int(mass) * C**2))
          
main()