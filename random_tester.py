import random

user_input = input("Enter a word or phrase: ")
big_letters = user_input.upper()
print("Your input in upper letters:", big_letters)

def create_anagram(word):
    # Can be used to remove spaces from the sentence
    #word_no_spaces = word.replace(" ", "")
    #char_list = list(word_no_spaces.lower())

    # Keeps the spaces in the sentence/word
    char_list = list(word.lower())
        
    # Shuffle the characters randomly
    random.shuffle(char_list)
    
    # Join the shuffled characters to form an anagram
    anagram = "".join(char_list)

    print(f"Anagram of your input is: {anagram}")


def print_opposite(word):
    opposite = word[::-1]
    print(f"Reversed order of the input is: {opposite}")


def reverse_word(word):

  #Set up a list for the word
  letter_list = []
  for letter in word:
    letter_list.append(letter)

  #Reverse the order of the list
  reversed_list = []
  for letter in range(len(letter_list)-1, -1, -1):
      reversed_list.append(letter_list[letter])

  #Format the list
  formatted_output = "".join(reversed_list)
  print(f"Reversed order of the input using another method is: {formatted_output}")


def count_letters(word):

    letter_count = {}
    
    for char in word:
        if char.isalpha(): 
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) +1

    print("Letter counts of the input:")
    for letter, count in letter_count.items():
        print(f"{letter}: {count}")

def total_letter_count(word):
    print(f"Number of letters in the input: {len(word)}")


create_anagram(user_input)
print_opposite(user_input)
reverse_word(user_input)
total_letter_count(user_input)
count_letters(user_input)


