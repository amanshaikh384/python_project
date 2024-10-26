import random

# Python Story Generator
def story_generator():
    print("Welcome to the Python Story Generator!")
    
    themes = ["fantasy", "mystery", "adventure", "science fiction", "romance"]
    chosen_theme = random.choice(themes)
    
    print(f"\nGenerating a {chosen_theme} story...\n")
    
    if chosen_theme == "fantasy":
        story = f"Once upon a time, in a mystical land, there was a brave knight named Sir {generate_name()}." \
                f" {generate_name()} was on a quest to retrieve the enchanted {generate_object()} and " \
                f"restore peace to the kingdom. Along the way, {generate_name()} encountered a magical " \
                f"creature, the {generate_creature()}. Will {generate_name()} be able to overcome the " \
                f"challenges and fulfill the prophecy? Only time will tell!"
    elif chosen_theme == "mystery":
        story = f"In the eerie town of {generate_location()}, a series of mysterious events unfolded. " \
                f"{generate_name()}, a brilliant detective, was called upon to solve the puzzling case. " \
                f"With the help of their loyal assistant, {generate_name()}, they delved into the " \
                f"shadows of the unknown. As the pieces of the puzzle came together, {generate_name()} " \
                f"unraveled a web of secrets and deception. Can they unveil the truth behind the " \
                f"{generate_mystery()} and bring justice to the town?"
    elif chosen_theme == "adventure":
        story = f"In the vast wilderness of {generate_location()}, a group of daring explorers set out " \
                f"on an epic adventure. Led by the fearless {generate_name()}, they sought the legendary " \
                f"{generate_treasure()} hidden in a forgotten temple. Along their perilous journey, " \
                f"{generate_name()} and their companions faced treacherous terrains, cunning traps, " \
                f"and fierce adversaries. Will they find the {generate_treasure()} and become the " \
                f"stuff of legends?"
    elif chosen_theme == "science fiction":
        story = f"In the distant future, humanity had colonized planets across the galaxy. In the " \
                f"{generate_star_system()}, a group of intrepid space explorers aboard the starship " \
                f"{generate_name()} embarked on a mission to investigate a peculiar anomaly. As they " \
                f"approached the enigmatic phenomenon, they encountered beings from another dimension. " \
                f"{generate_name()} and their crew must navigate through uncharted territories and " \
                f"unravel the mysteries of the cosmos."
    else:
        story = f"In a quaint town, two hearts intertwined as {generate_name()} met {generate_name()} " \
                f"by chance. A love story began to blossom amidst laughter and shared moments. " \
                f"As they explored life's adventures together, {generate_name()} and {generate_name()} " \
                f"discovered the magic of true love. Their love story would forever be etched in the " \
                f"fabric of time."

    print(story)

def generate_name():
    names = ["Alice", "Bob", "Eva", "David", "Luna", "Max", "Sophia", "Oliver", "Ava", "Noah", "Emma", "Leo"]
    return random.choice(names)

def generate_object():
    objects = ["sword", "amulet", "crystal", "staff", "key", "scroll"]
    return random.choice(objects)

def generate_creature():
    creatures = ["dragon", "unicorn", "phoenix", "mermaid", "elf", "troll"]
    return random.choice(creatures)

def generate_location():
    locations = ["Mysticville", "Shadowbrook", "Wanderwood", "Crystalhaven", "Twilight Vale"]
    return random.choice(locations)

def generate_mystery():
    mysteries = ["disappearing artifacts", "haunting spirits", "stolen jewels", "cryptic messages", "vanished city"]
    return random.choice(mysteries)

def generate_treasure():
    treasures = ["Lost Ark", "Eternal Orb", "Starlight Diamond", "Golden Chalice", "Cosmic Relic"]
    return random.choice(treasures)

def generate_star_system():
    star_systems = ["Alpha Centauri", "Sirius", "Vega", "Proxima Centauri", "Betelgeuse"]
    return random.choice(star_systems)

if __name__ == "__main__":
    story_generator()
