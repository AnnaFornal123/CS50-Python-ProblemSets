def main():
    userInput = input("Please, write something in upper case ")
    toLowerVoice(userInput)
    toSnakeCase(userInput)
    toCamelCase(userInput)

def toLowerVoice(sentence):
    print("TO LOWER: " + str.lower(sentence))

def toSnakeCase(sentence):
    print("TO SNAKE CASE ORIGINAL: " + str.replace(sentence, " ", "_"))
    print("TO SNAKE CASE LOWER: " + str.lower(sentence).replace(" ", "_"))

def toCamelCase(sentence):
    combined = str.lower(sentence).title().replace(" ", "")
    print(combined)

main()