import random

# Define a dictionary of animals and their descriptions
animals = {
    "dog": "A domesticated mammal known for its loyalty and companionship.",
    "cat": "A small carnivorous mammal often kept as a pet.",
    "elephant": "A large herbivorous mammal with a long trunk and tusks.",
    "giraffe": "A tall African mammal with a long neck and spotted coat.",
    "penguin": "A flightless bird native to the Southern Hemisphere.",
    "koala": "A marsupial native to Australia, known for its eucalyptus diet.",
    "lion": "A large carnivorous feline found in Africa and parts of Asia.",
    "tiger": "A powerful big cat known for its distinctive stripes.",
    "panda": "A bear native to China, recognized by its black and white fur.",
    "dolphin": "A highly intelligent marine mammal often seen swimming in oceans.",
    "cheetah": "The fastest land animal, known for its speed and spotted coat.",
}

def guess_animal():
    print("Welcome to the animal game!")
    print("Guess the animal from its description")
    print("Type 'quit' to exit the game. Let's get started!\n")
    

    animal = random.choice(list(animals.keys()))
    description = animals[animal]
    print(f"Description: {description}")

    while True: 
        guess = input("Your guess: ").lower()

        if guess == "quit":
            print("Game stopped, thanks for playing!")
            break
        elif guess == animal:
            print(f"Correct! The animal in question is {animal} as you guessed.")
            break
        else: 
            print("Incorrect. Try again!") 

if __name__ == "__main__":
    guess_animal()
