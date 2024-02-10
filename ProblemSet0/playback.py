def main():
    userInput = input("Please, write something ")
    slowDown(userInput)

def slowDown(sentence):
    print(str.replace(sentence, " ", "..."))

main()