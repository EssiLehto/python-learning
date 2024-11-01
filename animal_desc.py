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
    "horse": "A large, domesticated mammal often used for riding, racing, and work.",
    "kangaroo": "A marsupial native to Australia, known for its powerful hind legs and pouch.",
    "gorilla": "large, herbivorous primate found in African forests.", 
    "crocodile": "A reptile with a long snout, sharp teeth, and a tough, scaly skin, often found in freshwater habitats.", 
    "octopus": "A marine animal with eight arms, a soft body, and remarkable intelligence.", 
    "polar Bear": "A bear native to the Arctic regions, adapted for life in cold climates.", 
    "peacock": "A colorful bird with an impressive tail display, native to South Asia.", 
    "sloth": "A slow-moving mammal found in Central and South America, known for its leisurely lifestyle.", 
    "chimpanzee": "A highly intelligent primate, closely related to humans."
}


print("This is an animal dictionary. Here are the animals you can ask about:")
keys_list = list(animals.keys())
print(keys_list)

def print_animal_desc(animal):
    description = animals[animal]
    print(f"Description of a {animal}: {description}")

while True:
    user_input = input("Which animal you want to know more about? (input 'stop' to exit the dictionary) : ").lower()
    if user_input == "stop":
        print ("Thank you for using the dictionary!")
        break
    elif user_input in keys_list:
        print_animal_desc(user_input)
    else:
        print ("Animal does not exist in the dictionary.")