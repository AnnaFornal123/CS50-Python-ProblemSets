def main():
    userInput = input("Enter sentence containing :\) or :\(")
    convert(userInput)

def convert(sentence):
    happy = str.replace(sentence, ":)", "🙂")
    print(str.replace(happy, ":(", "🙁"))

main()