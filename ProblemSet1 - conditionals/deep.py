"""
In deep.py, 
implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. 
Otherwise output No.
"""

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    isAswerCorrect(answer)


def isAswerCorrect(input):
    match input.lower():
        case "forty-two" | "forty two" | "42":
            print("YES!")
        case _:
            print("No...")

main()