# Mad Libs Generator
def mad_libs_generator():
    print("Welcome to Mad Libs Generator!")
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")
    adverb1 = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    
    # Generate the story
    story = f"Once upon a time, there was a {noun1} that lived in a {adjective1} forest. " \
            f"One day, the {noun1} decided to {verb1} to the {noun2} {adverb1}. " \
            f"It was a {adjective2} adventure for the {noun1}!"
    
    print("\nYour Mad Libs Story:")
    print(story)

if __name__ == "__main__":
    mad_libs_generator()
