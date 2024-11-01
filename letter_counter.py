# Ask the user for input
user_input = input("Enter a word or phrase: ")

# Initialize an empty dictionary to store letters and their counts
letter_list = {}

# Iterate over each character in the input
for char in user_input:
    # Check if the character is a letter
    if char.isalpha():
        # Convert the letter to lowercase (to handle case-insensitivity)
        char = char.lower()
        # Update the letter count in the dictionary
        letter_list[char] = letter_list.get(char, 0) + 1

# Print the letter counts
print("Letter counts:")
for letter, count in letter_list.items():
    print(f"{letter}: {count}")
