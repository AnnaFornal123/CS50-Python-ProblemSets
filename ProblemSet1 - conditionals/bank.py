"""
In a file called bank.py, implement a program that prompts the user for a greeting. 
If the greeting starts with “hello”, output $0. 
If the greeting starts with an “h” (but not “hello”), output $20. 
Otherwise, output $100. 
Ignore any leading whitespace in the user's greeting, and treat the user's greeting case-insensitively.
"""

def main():
    greeting = get_greeting()
    reward = assess_greeting(greeting)
    print(f"Reward: $", str(reward))


def  get_greeting():
    return input("What's the greeting? ")


def assess_greeting(user_greeting):
    user_greeting = str.lower(user_greeting).strip()
    if user_greeting.startswith("hello"):
        return 0
    elif user_greeting.startswith("h"):
        return 20
    else:
        return 100


main()